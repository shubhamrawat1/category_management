
# How to run the project

1) Make Virtual Environment using "python3 -m venv <environment name>"
2) Install requirements using "pip install -r requirements.txt"
3) Run redis server to listen 
4) Commands to run Celery "celery -A category_management worker -l info" and "celery -A category_management beat -l info"
5) Now run "python manage.py makemigrations" and then "python manage.py migrate" to fill DB
6) Finally run "python manage.py runserver" to run the server 
