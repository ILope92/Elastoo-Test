# Sample code
[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://github.com/ILope92/Elastoo-Test/blob/master/LICENSE)

Проект подразумевает по [техническому заданию](https://github.com/ILope92/Elastoo-Test/blob/master/technical%20specification.txt) от компании Elastoo. Асинхронное приложение на веб-фреймворке aiohttp, включающее 2 логические части: API и worker.

## Оглавление
- [Описание проекта](#description)
    - [Worker](#worker)
    - [Endpoints](#endpoints)
- [Развернуть приложение](#deploy)
    - [Docker-compose](#docker)
    - [Запуск проекта](#start)
- [Подготовка к разработке](#dev)
- [API документация](#api)
- [Конфигурирование](#config)

<a name="description"></a>
## 1. Описание проекта
<a name="worker"></a>
## 1.1 Worker
Задачи выполняются последовательно, не параллельно. При добавлении задачи в очередь запоминает время создания задачи. После выполнения задачи удаляет задачу из очереди задач. Для сохранения задач и результата используется память


<hr>
<a name="endpoints"></a>

## 1.2 Endpoints
timeout используется перед добавлением числа (задачи) в список, то есть после того, как поступила новая задача, необходимо подождать timeout секунд и после поместить число в список. После этого задача считается выполненной и ее она удаляется из очереди задач

- [/add_task]() - Добавление задачи (на вход подается число и время ожидания). 
- [/get_result]() -Просмотр результата выполненных задач

- [/get_queue_work]() - список из актуальных (еще невыполненных) задач. Информация о каждой задачи включает:
    * номер в истории
    * время добавления
    * num
    * timeout

<hr>

## 2. Развернуть приложение

### 2.1 Docker-compose
<a name="deploy"></a>

Сборка проекта внутри Docker контейнера
```bash
~ docker-compose build
```
<hr>

### 2.2 Запуск проекта
<a name="start"></a>
```bash
~ docker-compose up
or
~ make compose
```
<hr>

<a name="dev"></a>

### 3. Подготовка к разработке

### Linux
```bash
~ make devenv
~ source env/bin/activate
(env) python -m main / make local_app
or
(env) docker-compose run -d -p 3000:8000 --name elastoo-application app
```
#### Windows
```bash
~ python -m venv env
~ .\env\Scripts\activate
(env) python -m pip install pip --upgrade
(env) python -m pip install -r requirements.txt
(env) python -m main
or
(env) docker-compose run -d -p 3000:8000 --name elastoo-application app
```
Данные команды установят виртуальное окружение, установят все необходимые зависимости, и произведут запуск проекта.
<hr>
<a name="api"></a>

### 4. API документация
* http://127.0.0.1:3000/api/docs/

<hr>
<a name="config"></a>

### 5. Конфигурирование
Вы можете указать HOST и PORT для запуска в docs/config_app.yaml, либо добавить аргументы в запуске:

    python -m main.py -H 127.0.0.2 -P 9090
