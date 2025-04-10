# Registration Project (Simple Django CRUD App)

This is a basic Django project implementing CRUD (Create, Read, Update, Delete) operations for a Registration table.

## Features:

- Add new users with Name, Email, and Date of Birth
- View list of registered users
- Update user information
- Delete users
- Simple HTML interface using Django templates
================================================================

## How to Run This Project

### 1. Clone the project
Or download the ZIP and extract it.

### 2. Navigate to project directory
```bash
cd registration_project_simple
```

### 3. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. Install Django
```bash
pip install django
```

### 5. Apply migrations to create the database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Open the app in your browser
Go to: `http://127.0.0.1:8000/`

================================================================
## Project Structure


registration_project_simple/
├── register/                  # Django app
│   ├── models.py              # Registration model
│   ├── views.py               # CRUD views
│   ├── urls.py                # App-specific routes
│   ├── templates/
│       └── register/
│           ├── list.html
│           ├── form.html
│           └── confirm_delete.html
├── registration_project/     # Django project config
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── db.sqlite3 (after migration)

==================================================================
## Default Database

SQLite (file-based, no setup needed)




