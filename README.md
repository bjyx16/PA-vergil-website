# PA-vergil-website

## Setting up venv:
python -m venv venv       
source venv/bin/activate

python manage.py runserver (run server locally)
http://127.0.0.1:8000/ 

python manage.py makemigrations bookcat

* be careful before migrating *
python manage.py migrate bookcat

open Django shell: 
python manage.py shell


## URLs in Django/html ##
{% url '<url path name>' <view_function_arguments> %}

superuser:
username: bailey
email: baileycishk@gmail.com
pin: pavergil2024