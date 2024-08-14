# PA-vergil-website
https://andover-catalog-vergiliana.azurewebsites.net/
<br> Please be patient, the site may take a while to load. Try reloading site if returns error.

## Basic Commands
**Setting up venv:**
<br> python3 -m venv venv       
source venv/bin/activate

pip freeze > requirements.txt

**Run server:**
<br> python manage.py runserver (run server locally): http://127.0.0.1:8000/ 

**Migrations:**  
python manage.py makemigrations bookcat  
(be careful before migrating): python manage.py migrate bookcat

**Open Django Shell:**  
python manage.py shell

**URLs in Django/html:**
{% url '<url path name>' <view_function_arguments> %}

### Notes:
To access data, download Vergil.xlsx

<!-- superuser:
username: bailey
email: baileycishk@gmail.com
pin: pavergil2024 -->
