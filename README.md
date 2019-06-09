# Laundry-App
Order management system built for laundry city.


## Install
- To change Database go to "DOMS/settings.py" and find "DATABASE = " then change database (visit here for more https://docs.djangoproject.com/en/1.10/ref/settings/#databases). Default Database is SQLite.

- Migrate Database by typing this:
```
foo@bar: python manage.py migrate
```
- Create new user by typing this:
```
foo@bar: python manage.py createsuperuser
```
- Install requirements by typing this:
```
foo@bar: pip install -r requirements.txt
```
- Run server by typing this:
```
foo@bar: python manage.py runserver
```
