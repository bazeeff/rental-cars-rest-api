# rental-cars-rest-api

### 1 Склонировать проект.
```console
git clone https://github.com/bazeeff/rental-cars-rest-api.git
```
### 2 Создать образ и запустить контейнер.
```console
sudo docker-compose up --build
```

### 3 Создать супер пользователя
```console
docker-compose exec web_run python manage.py createsuperuser
```

### 4 Зайти в панель администратора и создать токен пользователю для работы с API.

### 5 Конечные точки API, методы и примеры запросов:

Получить всех пользователей.

GET http://127.0.0.1:8000/api/users/


Получить информацию о пользователей и его машины.

GET http://127.0.0.1:8000/api/users/1/


Создание пользователя,добавление машин на этапе создания - опционально.

POST http://127.0.0.1:8000/api/users/

или 

POST http://127.0.0.1:8000/api/register/

json создание пользователя:
```json
{
    "email": "test_admin@mail.ru",
    "username": "test_admin",
    "password":"123qwe",
    "cars": []
}
```
Наличие полей: email,username,password,cars обязятально.


Обновление информации пользователя.

PUT http://127.0.0.1:8000/api/users/1/

json:
```json
{
    "email": "new_test_admin@mail.ru",
    "username": "new_test_admin",
    "password":"new_123qwe",
    "cars": []
}
```

Добавление машин пользователю.

PATCH http://127.0.0.1:8000/api/users/1/

json:
```json
{
    "email": "new_test_admin@mail.ru",
    "username": "new_test_admin",
    "password":"new_123qwe",
    "cars": [{"id":"1"},{"id":"2"} ]
}
```

Удаление пользователя.
DELETE http://127.0.0.1:8000/api/users/1/


Список машин.

GET http://127.0.0.1:8000/api/cars/


Просмотр информации об автомобиле.

GET http://127.0.0.1:8000/api/cars/1/


Создание машины.

POST http://127.0.0.1:8000/api/cars/

json:
```json
{
     "name": "ГАЗ-М-20 «Победа»",
     "created_date": "1946-01-01",
     "added_date": "2021-10-21"
}
```

Обновление инфомации о машине.

PATCH http://127.0.0.1:8000/api/cars/1/

json:
```json
{
     "name": "ГАЗ-3110 «Волга»",
     "created_date": "1997-01-01",
     "added_date": "2021-10-21"
}
```
Удаление машины.

DELETE http://127.0.0.1:8000/api/cars/1/


Взаимодействие через Browsable API аналогично вышеописанному.

### 7 Запуск тестов 
```console
python manage.py test
```


