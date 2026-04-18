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
