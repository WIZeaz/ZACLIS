@echo off
pip install django
pip install markdown
pip install pillow
pip install pygments
python manage.py makemigrations
python manage.py migrate
echo =========server ready for running=========
python manage.py runserver 0.0.0.0:80