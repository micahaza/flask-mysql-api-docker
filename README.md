mysql -v -u root --host=127.0.0.1 --port=32000 -p

# XAPO Test task README

Please note I only built Docker containers for develoment, so testing has to be done without docker. Also production configuraton and Docker containers I did not provide, in production it should be run with nginx + gunicorn for example.

## General requirements
* Create POST '/grab_and_save' endpoint
* Create GET '/last' endpoint
* Dockerize the app
* Create separate containers for flask app and database
* Connect two containers
* Use Flask-RESTful Flask extension
* Configure and initialize MySQL database
* Use SQLAlchemy 
* Use requests library to call external API
* Responses should be all in JSON
* There are some automated test suites for the app
* Curl could be used for testing

## POST '/grab_and_save' functionality
* The endpoint must accept a "currency" (ISO3 code, for example EUR, USD, BTC etc)
* The endpoint must accept an "amount", for example 100.23 or 0.25567801
* Code must call OpenExchangeRates API and grab the latest forex prices
* Register and use OpenExchangeRates API Key
* API Key is configurable
* Obtain the price for the currency passed in the POST request body

??? Multiply the price for the amount passed in the POST request body and obtain a final amount.

??? Store in MySQL the currency, the amount requested, the price given by open exchange rate and the final amount in USD

??? Use a precision of 8 decimal digits, and always round up. Do not loose precision in calculations!


## GET '/last' functionality
* this endpoint can be called alone, in which case it will return the last operation stored in MySQL
* or it can be passed a "currency" in which case you will need to return the last record for that specific currency from the MySQL DB
* or it can be called with a number (int) in which case it will return the last N operations
* or it can be called using both a currency and a number, in which case you will need to return the last N operations for that currency
* If currency is not supported we return a JSON error message

 

# How to install and run the app

# How to test the app with tox
Tox will run flake8 first for enforcing style consistency, then py.test to test the code.


## Curl example calls for external testing

