# Movie Management System App

This is a full-stack movie application built with Vue.js (frontend) and Django (backend), using PostgreSQL as the database.



## Prerequisites

- Git
- Node.js and npm
- Python 3.8 or above
- PostgreSQL

## Project Structure

project-root/
├── media # movie and thumbnail directory
├── vue-frontend/ # Vue.js frontend application
└── django-backend/ # Django backend application

## Setup Instructions
#### 1. Clone the repository
```
git clone https://github.com/koalaporings/your-repo-name
cd your-repo-name
```
### 2. Frontend Setup

```
cd vue-frontend
npm install
```
### 3. Backend Setup
```
cd ../django-backend
pip install -r requirements.txt
```

### 4. Install PostgreSQL

Download and install PostgreSQL from the official site:
https://www.postgresql.org/download/

### 5. Configure Database

1.  During PostgreSQL installation, create a user and set a password.

2.  Open `django-backend/mysite/settings.py`.

3.  Update the `DATABASES` section with your PostgreSQL username, password, and database name.

### 6. Apply Migrations
```
python manage.py migrate
```
### 7. Run the Application

#### Frontend
```
`cd ../vue-frontend
npm run serve`
```

#### Backend

```
cd ../django-backend
python manage.py runserver
```