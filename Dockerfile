from python:3
run pip install django==3.2
copy . .
RUN python3 manage.py makemigrations
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
