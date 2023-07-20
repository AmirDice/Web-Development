****STUDENT MANAGEMENT SYSTEM****
-----------
Login
----------
__ADMIN/HOD__
inuwaamir@zoho.com
password: admin

__STUDENT__
student@gmail.com
student

__STAFF__
staff@gmail.com
staff

-----------------------------
-----Installation Steps------
-----------------------------
__Project Dependency__

pip install requests
pip install Django
pip install mysql-client
pip install mysqlclient

First Create MySql Database
Change Database Setting in settings.py
---------------------
Run Migration Command 
---------------------
python manage.py makemigrations
python manage.py migrate

Run Project python runserver