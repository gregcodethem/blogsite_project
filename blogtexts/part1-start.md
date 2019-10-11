

$ mkdir blogsite_project

$ cd blogsite_project
$ mkdir blogsite
$ cd blogsite
$ cd ..

$ python3 -m venv env
$ source env/bin/activate
cd blogsite
$ pip install --upgrade pip

$ pip install wagtail

$ wagtail start blogsite .

$ python manage.py migrate
$ python manage.py createsuperuser
$ cd ..
$ git init

touch .gitignore
vi .gitignore
press i

*.pyc
*.DS_Store
env

press escape
:wq

$ cd blogsite
$ python manage.py runserver
ctrl + C
cd ..
git add .
git status

check everything's added

git commit -m "initial commit with functioning wagtail basic site"


Edit the home/templates/home/home_page.html:

{% block content %}
    <h1>{{ self.title }}</h1>
{% endblock %}

$ cd blogsite
$ python manage.py runserver
 

Visit http://127.0.0.1:8000/ and the homepage should have now changed.



