APP_PORT := 2202
DOCKER_TAG := latest

.PHONY: run_app
run_app:
	python3 -m uvicorn app:amazon_app --host='0.0.0.0' --port=$(APP_PORT)


.PHONY: install
install:
	pip install -r requirements.txt
	python3 -m pip install wemake-python-styleguide==0.16.1


.PHONY: download_weights
download_weights:
	dvc get git@gitlab.com:oliyyaa/cvr-hw1-modeling.git weights/ -o models/


.PHONY: lint
lint:
	PYTHONPATH=. flake8 src/


.PHONY: run_unit_tests
run_unit_tests:
	python -m pytest tests/unit