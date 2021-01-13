# Kitchen-Order
A Django web app that allows a manager create users as counter or kitchen staff. Counter staff can take orders. When orders are taken by counter staff, it is automatically sent in real-time to the pending screen of all kitchen staff. Kitchen staff can fulfil an order. Manager can see all orders, real-time.

# SetUp
- Clone Repo
- `cd Kitchen_Order`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser`
- `python3 manage.py runserver`
- Login to Admin Dashboard(`localhost:8000/admin`), and make the superuser you created a Manager.
- Log in to the app `localhost:8000`
