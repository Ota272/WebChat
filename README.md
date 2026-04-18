# Chat Webapp

## English

### Overview

A small **Django 6** web application: users pick a display name, then use a shared **chat room** with messages stored in **SQLite**. The UI uses **Bootstrap 5** (CDN). Authentication is **not** Django’s built-in user system: the app uses a custom `User` model (name only) and stores the selected user id in the **session**.

### Features

- **Registration** (`/`): enter a name; you are redirected to the chat and the session remembers your “user”.
- **Chat** (`/chat/`): post messages, **edit** your own messages (modal), **soft-delete** (archive) your messages.
- **Restore**: after you delete a message, it can be **restored** until **two or more new messages** have been created in the database since that deletion (then restore is no longer offered).
- **Date filter**: filter visible messages by date (GET query `date`).

### Tech stack

| Item        | Detail                                      |
|------------|----------------------------------------------|
| Framework  | Django 6.x                                   |
| Database   | SQLite (`db.sqlite3` next to `manage.py`)   |
| Frontend   | Bootstrap 5.3, server-rendered templates     |

### Project layout

- `chat_webapp/` — project settings and root URL config (`chat_webapp/urls.py`).
- `chat/` — app: models (`User`, `Message`), views, forms, templates (`register.html`, `chat.html`).

### How to run (development)

1. Create a virtual environment and install Django 6, for example:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install "Django>=6.0,<7"
   ```

2. Apply migrations and start the server:

   ```bash
   cd path\to\chat_webapp
   python manage.py migrate
   python manage.py runserver
   ```

3. Open `http://127.0.0.1:8000/` in a browser.

### Production / security notes

- `DEBUG = True` and a hard-coded `SECRET_KEY` in `settings.py` are suitable **only for local development**. For deployment, set a secret `SECRET_KEY`, turn `DEBUG` off, configure `ALLOWED_HOSTS`, and use a proper database and HTTPS as needed.
- There is **no** `requirements.txt` in the repo; pin dependencies yourself (e.g. `pip freeze`) for reproducible installs.

### Tests / admin

- `chat/tests.py` is a placeholder; add tests as you extend the app.
- Django admin is enabled at `/admin/` but models are not registered in `chat/admin.py` by default.

---

## Русский

### Обзор

Небольшое веб-приложение на **Django 6**: пользователь вводит **имя**, после чего попадает в **общую комнату чата**; сообщения хранятся в **SQLite**. Интерфейс — **Bootstrap 5** (CDN). **Не** используется стандартная система пользователей Django: есть своя модель `User` (только имя), идентификатор сохраняется в **сессии**.

### Возможности

- **Регистрация** (`/`): ввод имени, редирект в чат, сессия запоминает выбранного «пользователя».
- **Чат** (`/chat/`): отправка сообщений, **редактирование** своих сообщений (модальное окно), **мягкое удаление** (архивация).
- **Восстановление**: после удаления сообщение можно **вернуть**, пока с момента удаления не появилось **два и более новых сообщений** в базе — после этого восстановление скрывается.
- **Фильтр по дате**: отбор сообщений по дате (параметр GET `date`).

### Стек

| Компонент  | Детали                                      |
|-----------|---------------------------------------------|
| Фреймворк | Django 6.x                                  |
| БД        | SQLite (`db.sqlite3` рядом с `manage.py`)  |
| Фронт     | Bootstrap 5.3, шаблоны на сервере            |

### Структура проекта

- `chat_webapp/` — настройки проекта и корневой `urls.py`.
- `chat/` — приложение: модели (`User`, `Message`), представления, формы, шаблоны.

### Запуск (разработка)

1. Виртуальное окружение и Django 6, например:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install "Django>=6.0,<7"
   ```

2. Миграции и сервер:

   ```bash
   cd путь\к\chat_webapp
   python manage.py migrate
   python manage.py runserver
   ```

3. В браузере: `http://127.0.0.1:8000/`.

### Продакшен и безопасность

- `DEBUG = True` и постоянный `SECRET_KEY` в `settings.py` подходят **только для локальной разработки**. Для выкладки задайте секретный ключ, отключите отладку, настройте `ALLOWED_HOSTS`, при необходимости отдельную БД и HTTPS.
- В репозитории **нет** `requirements.txt`; зафиксируйте зависимости сами (например, `pip freeze`).

### Тесты и админка

- `chat/tests.py` — заглушка; тесты можно добавить по мере развития проекта.
- Админка Django доступна по `/admin/`, но модели в `chat/admin.py` по умолчанию не зарегистрированы.
