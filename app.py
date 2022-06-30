# Set up the Flask Weather App
# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
from requests import session
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create function allows access to SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect Database into classes
Base = automap_base()
# Reflect tables
Base.prepare(engine, reflect=True)
# Create variables
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create sesssion link from Python to SQLite database
session= Session(engine)
# Create a Flask application called "app"
app = Flask(__name__)

# Define welcome route
@app.route("/")
# Create function with a return statement
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Build route for precipitation analysis
@app.route("/api/v1.0/precipitation")
# Create the function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)




if __name__ == '__main__':
    app.run()