from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    return render_template('restaurant.html')


@app.route('/')
@app.route('/restaurant/new')
def newRestaurant():
    return render_template('newRestaurant.html')


@app.route('/')
@app.route('/restaurant/restaurant_id/edit')
def editRestaurant():
    return render_template('editRestaurant.html')


@app.route('/')
@app.route('/restaurant/restaurant_id/delete')
def deleteRestaurant():
    return render_template('deleteRestaurant.html')


@app.route('/')
@app.route('/restaurant/restaurant_id')
def showMenu():
    return render_template('menu.html')


@app.route('/')
@app.route('/restaurant/restaurant_id/menu/new')
def newMenuItem():
    return render_template('newMenuItem.html')


@app.route('/')
@app.route('/restaurant/restaurant_id/menu/menu_id/edit')
def editMenuItem():
    return render_template('editMenuItem.html')


@app.route('/')
@app.route('/restaurant/')
def deleteMenuItem():
    return render_template('deleteMenuItem.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
