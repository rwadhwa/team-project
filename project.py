import os
from flask import Flask, session, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    country = db.Column(db.Text)
    cars = db.relationship('Car', backref='manufacturer', cascade="delete")


class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.Integer)
    cartype = db.Column(db.String(256))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/members')
def members_page():
    return render_template('members.html')

@app.route('/cars')
def show_all_cars():
    cars = Car.query.all()
    return render_template('car-all.html', cars=cars)

@app.route('/inventory')
def get_all_cars():
    cars =[
    'M6',
    'S-Class',
    'Model-3'
    ]
    return render_template('inventory.html', cars = cars)

@app.route('/car/delete/<int:id>', methods=['GET', 'POST'])
def delete_course(id):
    car = Car.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('car-delete.html', car=car)
    if request.method == 'POST':
        db.session.delete(car)
        db.session.commit()
        return redirect(url_for('show_all_cars'))


@app.route('/car/edit/<int:id>', methods=['GET', 'POST'])
def edit_car(id):
    car = Car.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('car-edit.html', car=car)
    if request.method == 'POST':
        car.model = request.form['model']
        car.cartype = request.form['cartype']
        car.year = request.form['year']
        car.description = request.form['description']
        db.session.commit()
        return redirect(url_for('show_all_cars'))

@app.route('/car/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'GET':
        return render_template('car-add.html')
    if request.method == 'POST':
        model = request.form['model']
        cartype = request.form['cartype']
        year = request.form['year']
        description = request.form['description']
        car = Car(model=model, cartype=cartype, year=year, description=description)
        db.session.add(car)
        db.session.commit()
        return redirect(url_for('show_all_cars'))

@app.route('/manufacturers')
def show_all_manufacturers():
    manufacturers = Manufacturer.query.all()
    return render_template('manufacturer-all.html', manufacturers=manufacturers)

@app.route('/manufacturer/delete/<int:id>', methods=['GET', 'POST'])
def delete_manufacturer(id):
    manufacturer = Manufacturer.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('manufacturer-delete.html', manufacturer=manufacturer)
    if request.method == 'POST':
        db.session.delete(manufacturer)
        db.session.commit()
        return redirect(url_for('show_all_manufacturers'))


@app.route('/manufacturer/edit/<int:id>', methods=['GET', 'POST'])
def edit_manufacturer(id):
    manufacturer = Manufacturer.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('manufacturer-edit.html', manufacturer=manufacturer)
    if request.method == 'POST':
        manufacturer.name = request.form['name']
        manufacturer.country = request.form['country']
        db.session.commit()
        return redirect(url_for('show_all_manufacturers'))

@app.route('/manufacturer/add', methods=['GET', 'POST'])
def add_manufacturer():
    if request.method == 'GET':
        return render_template('manufacturer-add.html')
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        manufacturer = Manufacturer(name=name, country=country)
        db.session.add(manufacturer)
        db.session.commit()
        return redirect(url_for('show_all_manufacturers'))

if __name__ == '__main__':
    app.run(debug=True)
