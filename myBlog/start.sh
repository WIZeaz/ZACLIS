pip install django
pip install markdown
pip install pillow
pip install pygments
python3 manage.py makemigrations
python3 manage.py migrate
nohup python3 manage.py runserver 0.0.0.0:80 > server.stdout 2> server.stderr & disown
