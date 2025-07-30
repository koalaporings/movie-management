# Movie Management System App

This is a full-stack movie application built with Vue.js (frontend) and Django (backend), using PostgreSQL as the database.



## Prerequisites

- Git
- Node.js and npm
- Python 3.8 or above
- PostgreSQL

## Project Structure
```
project-root/
├── media # movie and thumbnail directory
├── vue-frontend/ # Vue.js frontend application
└── django-backend/ # Django backend application
```

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

2.  Open the psql CLI included in the installation.

3.  Press ENTER until you reach the password section.

4.  After giving your password and pressing ENTER, write this command in the CLI.

    `CREATE DATABASE movie_management`

5.  Open `django-backend/mysite/settings.py`.


6.  Update the `DATABASES` section with your PostgreSQL username, password, and database name.
Example:
```
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_management',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
```

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

## Known Bugs and Issues

1. When updating a movie, the `thumbnail` and `video file` upload fields are not filled up immediately, causing the user to reupload the files used.

2. When viewing a movie, then going back to the home page and try to delete said movie, it will result in an error.

## Suggested Improvements

1. Implement a celery task to convert any movie/video file into the .mp4 format after creating/uploading. The uploaded movie will not be seen in the movie list until the conversion is completed, to ensure better playback and audio.

2. Implement thumbnail generation for the video player to preview a scene in the selected movie.

## Testing Instructions

#### File Upload
    1. Login using a registered user.
    2. Click the Upload button in the navigation header.
    3. Fill up the input fields.
    4. Upload your thumbnail/poster.
    5. Upload your video file.
    6. Press Submit.
    7. Wait for success modal to appear.
    8. Close the success modal and check if movie appears in the movie list.

#### Movie Update
    1. Login using a registered user.
    2. Click the Update button beside a movie.
    3. Fill up the input fields needed to be updated
    4. Upload your thumbnail/poster.
    5. Upload your video file.
    6. Press Submit.
    7. Wait for success modal to appear.
    8. Close the success modal.
    9. Look for the movie in the movie list.
    10. Click the View button beside the update movie.
    11. Check the right-side of the page for the details of the movie.

#### Video Playback
    1. Login using a registered user.
    2. Click the View button beside a movie.
    3. Play the video at the right-side of the page.