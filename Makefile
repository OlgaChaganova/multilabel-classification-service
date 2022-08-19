DVC_REMOTE_NAME := dvc_remote_staging
USERNAME: oliyyaa

APP_PORT := 2202
DOCKER_TAG := latest



.PHONY: run_app
run_app:
	python3 -m uvicorn app:amazon_app --host='0.0.0.0' --port=$(APP_PORT)


.PHONY: install
install:
	pip install -r requirements.txt
	python3 -m pip install wemake-python-styleguide==0.16.1


.PHONY: install_c_libs
install_c_libs:
	apt-get update && apt-get install -y --no-install-recommends gcc ffmpeg libsm6 libxext6


.PHONY: init_dvc
init_dvc:
	dvc init --no-scm
	dvc remote add --default $(DVC_REMOTE_NAME) ssh://91.206.15.25/home/$(USERNAME)/dvc_files
	dvc remote modify $(DVC_REMOTE_NAME) user $(USERNAME)
	dvc config cache.type hardlink,symlink


.PHONY: download_weights_ssh
download_weights_ssh:
	dvc get git@gitlab.com:oliyyaa/cvr-hw1-modeling.git weights/ -o models/


.PHONY: download_weights_dvc
download_weights_dvc:
	dvc pull -R weights
	mv weights/*.pt models/


.PHONY: lint
lint:
	PYTHONPATH=. flake8 src/


.PHONY: run_unit_tests
run_unit_tests:
	python -m pytest tests/unit


.PHONY: run_integration_tests
run_integration_tests:
	python -m pytest tests/integration


.PHONY: run_tests
run_tests:
	make run_unit_tests
	make run_integration_tests
