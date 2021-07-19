all:
	@echo "make app			- Start app container"
	@echo "make local_app	- Start app local"
	@echo "make devenv      - install enviroment python3.9"
	@echo "make compose     - build and run app, db services"
	@echo "make clean     	- clean cache"
	@exit 0

clean: clean_cache
	rm -fr *.egg-info dist

clean_cache:
	rm -fr application/__pycache__
	rm -fr application/models/__pycache__
	rm -fr application/middlewares/__pycache__
	rm -fr application/responses/__pycache__
	rm -fr application/utils/__pycache__

devenv: clean
	rm -rf env
	# создаем новое окружение
	apt-get install python3-venv
	python3.9 -m venv env
	env/bin/python3.9 -m pip install pip --upgrade
	env/bin/python3.9 -m pip install wheel
	# ставим зависимости
	env/bin/python3.9 -m pip install -r requirements.txt

compose:
	sudo docker-compose up --build -d

app:
	docker stop elastoo-application || true
	docker-compose run -d -p 3000:8000 --name elastoo-application app

local_app:
	python -m main.py