# Barter Platform
Простая платформа для обмена вещами между пользователями. Позволяет размещать объявления, искать по фильтрам и отправлять предложения на обмен. Пользователи должны быть авторизованы для использования всех функций сайта.

## Возможности
Регистрация и вход пользователей

Создание, редактирование, удаление объявлений

### Категории: 
* Cпорт
* Ремонт
* Техника
* Кухня
* Автомобиль
* Другое

Поиск по ключевым словам, фильтрация по категории и состоянию

Предложения обмена между пользователями

Интерфейс авторизации / регистрации через Django auth

Панель администратора

REST API через Django REST Framework (опционально)

Установка
Клонируйте репозиторий:

    git clone https://github.com/your-username/barter-platform.git
    cd barter-platform

Создайте и активируйте виртуальное окружение:

    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

Установите зависимости:

    pip install django djangorestframework


Настройка базы данных
По умолчанию используется PostgreSQL:

    # settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'trade_tz',
            'USER': 'postgres',
            'PASSWORD': 'ваш_пароль',
            'HOST': 'localhost',
            'PORT': '5433',
        }
    }

Создайте базу:

    CREATE DATABASE trade_tz;
    CREATE USER postgres WITH PASSWORD '1234';
    GRANT ALL PRIVILEGES ON DATABASE trade_tz TO postgres;

Запуск проекта

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser  # создайте админа
    python manage.py runserver

Перейдите в браузере: http://127.0.0.1:8000/

URL-структура
URL	Назначение
/	Главная (список объявлений)
/ads/create/	Создание объявления
/ads/<id>/	Просмотр объявления
/ads/<id>/edit/	Редактирование объявления
/ads/<id>/delete/	Удаление объявления
/proposals/	Список предложений
/proposals/create/	Создание предложения
/register/	Регистрация пользователя
/login/	Вход
/logout/	Выход
/admin/	Панель администратора
/api/ads/, /api/proposals/	(если используется DRF)
/swagger/	Swagger-документация (опционально)

Тестирование

    python manage.py test ads

Покрытие тестами:

Регистрация и вход

CRUD объявлений

Проверка авторства

Создание предложений

Поиск и фильтрация

Стек
Python 3.8+

Django 4+

PostgreSQL

Django Templates + Bootstrap 5

Django REST Framework (опционально)

drf-yasg (Swagger, опционально)

Примечания
Все действия с объявлениями и предложениями доступны только авторизованным пользователям.

Форма регистрации доступна всем по /register/

В шаблонах реализована адаптивная навигация

SWAGGER-документация

    Доступна по адресу: `/swagger/`

    Позволяет тестировать и просматривать REST API:
    - `GET /api/ads/`
    - `POST /api/proposals/`
    и т.д.

Лицензия
Проект распространяется под лицензией MIT.
