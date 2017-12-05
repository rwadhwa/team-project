from flask_script import Manager
from project import app, db, Manufacturer, Car


manager = Manager(app)


@manager.command ## populate database with real data
def deploy():
    db.drop_all()
    db.create_all()
    man1 = Manufacturer(manuf='BMW', country='Germany')
    man2 = Manufacturer(manuf='Mercedes', country='Germany')
    man3 = Manufacturer(manuf='Tesla', country='United States of America')
    car1 = Car(model='M6', type='Coupe', year='2015', manuf='BMW', description="One of BMWs best performance cars.")
    car2 = Car(model='S Class', type='Sedan', year='2013', manuf='Mercedes', description="The ultimate Mercedes in terms of luxary.")
    car3 = Car(model='Model 3', type='Electric', year='2018', manuf='Tesla', description="The worlds first premium electric car under $40,000.")
    db.session.add(man1)
    db.session.add(man2)
    db.session.add(man3)
    db.session.add(car1)
    db.session.add(car2)
    db.session.add(car3)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
