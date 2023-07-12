# FastAPI Messaging App

1. A REST API that receives a single message and that updates a statistics table 
on a relational database. 
2. A REST API that provides statistical information back to the reader.


## Installation
To run the project in your local environment::
Clone the repository::
Create and activate a virtual environment::
  $ python -m venv venv
  $ source venv/bin/activate
Install requirements::  
  $ pip install -r requirements.txt

Create/update .env and set variables

Run the application::
  $ uvicorn main:app --reload


## Tests
Test are run with pytest. If you are not familiar with this package you can get some more info from their website <https://pytest.org/>_.

To run the tests, from the project directory, simply::
$ pytest -v
