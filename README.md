## Run server
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py runserver


## Test
python manage.py test api.tests

## Coverage
```
1. coverage run manage.py test api -v 2
2. coverage html
3. open kami_airlines/htmlcov/index.html
```
