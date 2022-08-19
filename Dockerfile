from python:3
run pip install django==3.2
copy . .
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
