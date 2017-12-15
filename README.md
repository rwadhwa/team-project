# team-project
Project by George Thuku, Raveena Wadhwa, and Parth Patel. Our project is a car database.
The car database will contain two tables, the first being a car table and the second being the manufacturer table. The connection will be the manufacturer name, and have a one to many relationship. The fields in the car table will be carID, manufacturer name, car type, year, and description. The fields in the manufacturer table will be manufacturer's name, and manufacturer's country.

## Car Table  :

Car ID | Manufacturer Name | Model | Car Type | Year | Description
------| -------------| --------|------|----------|---------|
1 | BMW |  M6 | Coupe | 2015 | One of BMWs best performance cars.
2 | Mercedes | S Class | Sedan | 2013 | The ultimate Mercedes in terms of luxury.
3 | Tesla |Model 3 | Electric | 2018 | The worlds first premium electric car under $40,000.

## Manufacturer Table:

Manufacturer Name | Country
------------------|--------
BMW | Germany
Mercedes | Germany
Tesla | United States


## To Run the Application

### Install necessary virtual environment file:

  *$ virtualenv venv*

### Activate the virtual environment:

  *$ source venv/bin/activate*

### Install necessary packages

  *$ pip install -r requirements.txt*

### Initialize the database

  *$ python manage.py deploy*

### Run the development server with the debugger on

  *$ python manage.py runserver -d*
