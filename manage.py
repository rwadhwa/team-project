from flask_script import Manager
from project import app, db, Manufacturer, Car


manager = Manager(app)


@manager.command ## populate database with real data
def deploy():
    db.drop_all()
    db.create_all()
    manufacturer1 = Manufacturer(name='BMW', country='Germany')
    manufacturer2 = Manufacturer(name='Mercedes', country='Germany')
    manufacturer3 = Manufacturer(name='Tesla', country='United States of America')
    car1 = Car(model='M6', cartype='Coupe', year='2015', description='One of BMWs best performance cars.', manufacturer=manufacturer1)
    car2 = Car(model='S Class', cartype='Sedan', year='2013', description='The ultimate Mercedes in terms of luxary.', manufacturer=manufacturer2)
    car3 = Car(model='Model 3', cartype='Electric', year='2018', description='The worlds first premium electric car under $40,000.', manufacturer=manufacturer3)
    db.session.add(manufacturer1)
    db.session.add(manufacturer2)
    db.session.add(manufacturer3)
    db.session.add(car1)
    db.session.add(car2)
    db.session.add(car3)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
