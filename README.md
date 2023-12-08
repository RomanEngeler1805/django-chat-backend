# django-chat-backend
## Setup
Create and activate a virtual environment in the main project folder
'''python3 -m venv <name of virtual environment>¨
source venv/bin/activate'''

Install the requirements
'''pip install -r requirements.txt'''

Save the via email received firestore credentials in the main project folder
Set the environment variable
'''export GOOGLE_APPLICATION_CREDENTIALS=<path to credentials file>'''

## Run the application
Navigate into the '''backend''' folder and run
'''python manage.py runserver 8080'''