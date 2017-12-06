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

@app.route('/manufacturers')
def show_all_manufacturers():
    manufacturers = Manufacturer.query.all()
    return render_template('manufacturer-all.html', manufacturers=manufacturers)

if __name__ == '__main__':
    app.run(debug=True)
