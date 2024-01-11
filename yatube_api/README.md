
api final
# Yatube API

Yatube API - это Django REST framework проект для создания API для социальной сети.

## Установка

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/Wayer5/api_final_yatube.git
cd API_FINAL_YATUBE

Cоздать и активировать виртуальное окружение:

python -m venv venv
source venv/bin/activate

Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:

python manage.py migrate

Запустить проект:

python manage.py runserver

## Использование
Для работы с API, используйте пути /api/v1/, например, /api/v1/posts/, /api/v1/groups/, и так далее.

Для аутентификации и получения токена, используйте эндпоинты /api/v1/jwt/create/ и /api/v1/jwt/refresh/.

Эндпоинты
/api/v1/posts/: Получение списка всех публикаций или создание новой публикации.
/api/v1/posts/{id}/: Получение, обновление или удаление конкретной публикации.
/api/v1/posts/{post_id}/comments/: Получение списка всех комментариев к публикации или создание нового комментария.
/api/v1/posts/{post_id}/comments/{id}/: Получение, обновление или удаление конкретного комментария к публикации.
/api/v1/groups/: Получение списка всех сообществ или создание нового сообщества.
/api/v1/groups/{id}/: Получение информации о конкретном сообществе.
/api/v1/follow/: Получение списка подписок пользователя или создание новой подписки.