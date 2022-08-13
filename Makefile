APP_PORT := 2202
DOCKER_TAG := latest

.PHONY: run_app
run_app:
	python3 -m uvicorn app:app --host='0.0.0.0' --port=$(APP_PORT)


.PHONY: install
install:
	pip install -r requirements.txt


.PHONY: download_weights
download_weights:
	dvc pull -R weights
