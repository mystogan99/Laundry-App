# Laundry-App
Order management system built for laundry city.

## Install

- Install requirements by typing this:
```
foo@bar:~$ pip install -r requirements.txt
```
- Migrate Database by typing this:
```
foo@bar:~$ python manage.py migrate
```
- Create new user by typing this:
```
foo@bar:~$ python manage.py createsuperuser
```
- Run server by typing this:
```
foo@bar:~$ python manage.py runserver
```
- Reset port by typing:
```
foo@bar:~$ sudo fuser -k 8000/tcp
```
## Features
- Add order
- Add order category
- Export Order (pdf, excel, csv and etc)
- Update/ Delete Order
- Print Invoice
- Login

