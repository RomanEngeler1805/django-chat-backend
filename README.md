# django-chat-backend
## Setup
### Create and activate a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### Install the requirements
```
pip install -r requirements.txt
```

### Set environment variables
Save the via email received firestore credentials in the main project folder
Set the environment variable
```
export GOOGLE_APPLICATION_CREDENTIALS='PATH_TO_CREDENTIALS.json'
```

## Run the application
Navigate into the /backend folder and run
```
python manage.py runserver 8080
```
