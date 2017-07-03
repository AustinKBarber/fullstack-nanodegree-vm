from database_setup import Base, Restaurant, MenuItem
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    return render_template(restaurant.html, restaurants=restaurants)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
