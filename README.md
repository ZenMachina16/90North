# Chat Application

A real-time chat application built with Django. This application allows users to sign up, log in, and communicate with other users in real-time using WebSockets.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd chat_project
```

### 2. Create a Virtual Environment
#### Using `virtualenv`:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Configure the Database
By default, the project uses SQLite. If you'd like to use another database, update the `DATABASES` setting in `chat_project/settings.py`.

Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to set up admin credentials.


### 6. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

---

## Project Structure

```plaintext
Directory structure:
└── zenmachina16-90north/
    ├── db.sqlite3
    ├── manage.py
    ├── requirement.txt
    ├── chat/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── consumers.py
    │   ├── models.py
    │   ├── routing.py
    │   ├── tests.py
    │   ├── urls.py
    │   └──views.py
    ├── chat_app/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └──wsgi.py
    │   
    ├── templates/
    │   ├── chat.html
    │   ├── login.html
    │   └── signup.html
    └── users/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        └──  views.py
        
      
