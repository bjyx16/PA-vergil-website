# PA-vergil-website

## Basic Commands
Setting up venv:  
python -m venv venv       
source venv/bin/activate

Run server:  
python manage.py runserver (run server locally): http://127.0.0.1:8000/ 

Migrations:  
python manage.py makemigrations bookcat  
**be careful before migrating**  
python manage.py migrate bookcat

Open Django Shell:  
python manage.py shell

URLs in Django/html:
{% url '<url path name>' <view_function_arguments> %}

<!-- superuser:
username: bailey
email: baileycishk@gmail.com
pin: pavergil2024 -->
