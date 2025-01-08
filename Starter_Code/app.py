import pandas as pd
from flask import Flask, jsonify
from sql_helper import SQLHelper

##################################################################################
# Flask Setup
##################################################################################

app = Flask(__name__)
sqlHelper = SQLHelper()


##################################################################################
# Flask Routes
##################################################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"<a href='/api/v1.0/tobs' target='_blank'>/api/v1.0/tobs</a><br/>"
        f"<a href='/api/v1.0/2017-01-01' target='_blank'>/api/v1.0/2017-01-01</a><br/>"
        f"<a href='/api/v1.0/2017-01-01/2017-01-31' target='_blank'>/api/v1.0/2017-01-01/2017-01-31</a><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Execute queries
    precipitation_df = sqlHelper.queryPrecipitation()

    # Turn DataFrame into List of Dictionary
    data = precipitation_df.to_dict(orient ='records')
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    # Execute queries
    stations_df = sqlHelper.queryStations()

    # Turn DataFrame into List of Dictionary
    data = stations_df.to_dict(orient ='records')
    return jsonify(data)


@app.route("/api/v1.0/tobs")
def queryTemperature():
    # Execute queries
    temperature_df = sqlHelper.queryTemperature()

    # Turn DataFrame into List of Dictionary
    data = temperature_df.to_dict(orient ='records')
    return jsonify(data)

@app.route("/api/v1.0/<start>")

def queryTempstats(start):
    # Execute queries
    temperature_stats_df = sqlHelper.queryTempstats(start)

    # Turn DataFrame into List of Dictionary
    data = temperature_stats_df.to_dict(orient ='records')
    return jsonify(data)


@app.route("/api/v1.0/<start>/<end>")                       
def queryTempstats_startend(start, end):

    # Execute queries
    temperature_stats_StartEnd_df= sqlHelper.queryTempstats_startend(start, end)

    # Turn DataFrame into List of Dictionary
    data = temperature_stats_StartEnd_df.to_dict(orient ='records')
    return jsonify(data)                            

if __name__ == '__main__':
    app.run(debug=True)