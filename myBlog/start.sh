pip install django
py3 manage.py makemigrations
py3 manage.py migrate
nohup py3 manage.py runserver > server.stdout 2>server.stderr & disown
