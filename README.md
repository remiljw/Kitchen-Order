# Kitchen-Order
A Django web app that allows a manager create users as counter or kitchen staff. Counter staff can take orders. When orders are taken by counter staff, it is automatically sent in real-time to the pending screen of all kitchen staff. Kitchen staff can fulfil an order. Manager can see all orders, real-time.

# SetUp
- Clone Repo
- Create a virual environment using venv or virual env and activate it.
- `cd Kitchen_Order`
-  run `pip install -r requirements.txt`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser`
- `python3 manage.py runserver`
- Login to Admin Dashboard(`localhost:8000/admin`), and make the superuser you created a Manager.
- Log in to the app `localhost:8000`

Or use login details below.
# Login Details
### Superuser and Manager
- username: michael
- password: manager