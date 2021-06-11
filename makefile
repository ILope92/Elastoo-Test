PROJECT_NAME ?= unnamed
VERSION = $(shell python3 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= lening
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make clean		- Remove files created by distutils"
	@echo "make dev      	- install enviroment python3.8"
	@exit 0

clean: clean_cache
	rm -fr *.egg-info dist

clean_cache:
	rm -fr application/__pycache__
	rm -fr application/models/__pycache__
	rm -fr application/middlewares/__pycache__
	rm -fr application/responses/__pycache__
	rm -fr application/utils/__pycache__

dev: clean
	rm -rf env
	apt-get install python3-venv
	python3.8 -m venv env
	env/bin/python3.8 -m pip install pip --upgrade
	env/bin/python3.8 -m pip install wheel
	env/bin/python3.8 -m pip install -r requirements.txt

env_delete:
	rm -fr env
	rm -fr .vscode

run_dev: dev
	env/bin/python3.8 run_app.py

run:
	python3.8 run_app.py