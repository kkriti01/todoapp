Install:
--------------------
pip install -r requirements.pip

Run
---
python manage.py makemigrations

python manage.py migrate
    
    test on local server run
    -----------------
    python manage.py runserver

urls to test
-------------------
localhost:8000/todo_list ---see the task

localhost:8000/todo  -------create the task

localhost:8000/todo_update -------update the task

localhost:8000/register ---------register user

localhost:8000/login --------authentication