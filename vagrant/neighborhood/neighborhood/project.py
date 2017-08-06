from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Locations, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


APPLICATION_NAME = "Category Menu App"

# Connect to Database and create database session
engine = create_engine('sqlite:///locations.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# @app.route('/locations/')
# def showLocations():
#     locations = session.query(Locations).order_by(asc(Locations.name))
#     return render_template('index.html', locations=locations)
    # if 'username' not in login_session:
    #     return render_template('publiccategories.html', categories=categories)
    # else:
    #     return render_template('index.html', locations=locations)

@app.route('/')
def renderShit():
    return render_template('index.html')

# Create a new location

@app.route('/locations', methods=['GET', 'POST'])
def newLocation():
    newLocation = Locations(name=request.form['name'], lat=request.form['lat'], long=request.form['long'],
                            user_id=request.form['user_id'])
    session.add(newLocation)
    flash('New location %s Successfully Created' % newLocation.name)
    session.commit()


# else:
#    return render_template('newCategory.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
