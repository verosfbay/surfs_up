# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# Now let's reflect the database into our classes.
Base = automap_base()
Base.prepare(engine, reflect=True)

# With the database reflected, we can save our references to each table. 
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database with the following code:
session = Session(engine)

# Set Up Flask
app = Flask(__name__)


