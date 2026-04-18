# 💬 Django Light WebChat

A lightweight, session-based web chat application built with Python and Django. This project demonstrates core backend development concepts including MVC architecture, database modeling, form handling, and session management.

## ✨ Features

- **Session-Based Authentication:** Users can join the chat simply by entering their name. The session is maintained using Django's built-in session framework, ensuring a frictionless onboarding experience.
- **Message CRUD Operations:** Users can send, read, and edit their own messages in the chat room.
- **Soft Delete Mechanism:** Instead of permanently deleting records from the database, messages are marked as "archived". Users can view their archived messages and restore them at any time.
- **Responsive UI:** Clean and modern interface built with Bootstrap 5, featuring modal windows for editing and alert messages for user feedback.

## 🛠️ Tech Stack

- **Backend:** Python 3, Django 6.0
- **Database:** SQLite (default)
- **Frontend:** HTML5, CSS3, Bootstrap 5, Vanilla JavaScript
- **Architecture:** MVT (Model-View-Template)

## 🗂️ Project Structure

The core logic of the application is located in the `chat` app:
- `models.py`: Defines the `User` and `Message` database schemas.
- `views.py`: Handles business logic for registration, chat display, message editing, archiving, and restoration.
- `forms.py`: Utilizes Django `ModelForm` for clean data validation and widget rendering.
- `templates/`: Contains the UI layers (`chat.html`, `register.html`).

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python installed on your system.
```bash
python --version
Installation
Clone the repository:

Bash
git clone [https://github.com/yourusername/django-light-webchat.git](https://github.com/yourusername/django-light-webchat.git)
cd django-light-webchat/chat_webapp
Create and activate a virtual environment (recommended):

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install Django:
Bash
pip install django

Apply database migrations:
Bash
python manage.py migrate

Run the development server:
Bash
python manage.py runserver
Open your browser:
Navigate to http://127.0.0.1:8000/ to start chatting!

💡 How It Works
Registration: Upon visiting the root URL, you are prompted to enter a name. A User object is created, and your unique ID is stored securely in the browser's session.

Chat Room: You are redirected to the chat room where all active (non-archived) messages are ordered by timestamp.

Message Management: - Clicking Edit opens a Bootstrap modal populated with the message text via JavaScript data attributes.

Clicking Delete archives the message, removing it from the main thread and placing it in the "Archived messages" section at the bottom of the page, where it can be restored.

🔮 Future Improvements
While this project is fully functional as a standard HTTP request/response application, planned future upgrades include:

Integrating Django Channels and Redis for full WebSockets support, allowing true real-time, asynchronous messaging.

Expanding authentication to support secure user accounts with passwords via django.contrib.auth.

Building out a REST API using Django REST Framework (DRF) or FastAPI for mobile client support.

## Описание на русском

💬 Django Light WebChat
Легкое веб-приложение для чата на основе сессий, созданное с использованием Python и Django. Этот проект демонстрирует основные концепции бэкенд-разработки, включая архитектуру MVC, моделирование баз данных, обработку форм и управление сессиями.

✨ Функции
Аутентификация на основе сессий: Пользователи могут присоединиться к чату, просто введя свое имя. Сессия поддерживается с помощью встроенного фреймворка сессий Django, что обеспечивает максимально простой вход.

CRUD операции для сообщений: Пользователи могут отправлять, читать и редактировать свои собственные сообщения в чат-комнате.

Механизм мягкого удаления (Soft Delete): Вместо безвозвратного удаления записей из базы данных, сообщения помечаются как «архивированные». Пользователи могут просматривать свои архивные сообщения и восстанавливать их в любое время.

Адаптивный интерфейс: Чистый и современный интерфейс, построенный на Bootstrap 5, с использованием модальных окон для редактирования и всплывающих уведомлений для обратной связи.

🛠️ Стек технологий
Бэкенд: Python 3, Django 6.0

База данных: SQLite (по умолчанию)

Фронтенд: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript

Архитектура: MVT (Model-View-Template)

🗂️ Структура проекта
Основная логика приложения находится в папке chat:

models.py: Определяет схемы базы данных для User и Message.

views.py: Обрабатывает бизнес-логику регистрации, отображения чата, редактирования, архивирования и восстановления сообщений.

forms.py: Использует Django ModelForm для валидации данных и рендеринга виджетов.

templates/: Содержит слои пользовательского интерфейса (chat.html, register.html).

🚀 Начало работы
Следуйте этим инструкциям, чтобы запустить копию проекта на локальном компьютере для разработки и тестирования.

Предварительные требования
Убедитесь, что в вашей системе установлен Python.

Bash
python --version
Установка
Клонируйте репозиторий:

Bash
git clone https://github.com/yourusername/django-light-webchat.git
cd django-light-webchat/chat_webapp
Создайте и активируйте виртуальное окружение (рекомендуется):

Bash
python -m venv venv
# На Windows:
venv\Scripts\activate
# На macOS/Linux:
source venv/bin/activate
Установите Django:

Bash
pip install django
Примените миграции базы данных:

Bash
python manage.py migrate
Запустите сервер разработки:

Bash
python manage.py runserver
Откройте браузер:
Перейдите по адресу http://127.0.0.1:8000/, чтобы начать общение!

💡 Как это работает
Регистрация: При посещении корневого URL-адреса вам будет предложено ввести имя. Создается объект User, и ваш уникальный ID надежно сохраняется в сессии браузера.

Чат-комната: Вы перенаправляетесь в чат, где все активные (неархивированные) сообщения упорядочены по времени.

Управление сообщениями: - Нажатие на Edit открывает модальное окно Bootstrap, заполненное текстом сообщения через JavaScript-атрибуты данных.

Нажатие на Delete архивирует сообщение, удаляя его из основной ветки и помещая в раздел «Архивные сообщения» в нижней части страницы, откуда его можно восстановить.

🔮 Будущие улучшения
Хотя этот проект полностью функционален как стандартное приложение на HTTP-запросах, планируемые обновления включают:

Интеграция Django Channels и Redis для полноценной поддержки WebSockets (сообщения в реальном времени).

Расширение аутентификации для поддержки защищенных учетных записей с паролями через django.contrib.auth.

Создание REST API с использованием Django REST Framework (DRF) или FastAPI для поддержки мобильных клиентов.
