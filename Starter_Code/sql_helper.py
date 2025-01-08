# Import Python SQL toolkit and Object Relational Mapper
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func

import pandas as pd
import datetime

# Define the SQLHelper Class
# PURPOSE: Deal with all of the database logic

class SQLHelper():

# Initialize PARAMETERS/VARIABLES

################################################################################### 
#Database Setup
###################################################################################
    def __init__(self):
        self.engine = create_engine(f"sqlite:///Resources/hawaii.sqlite")
        self.Station = self.createStation()
        self.Measurement = self.createMeasurement()

    def createStation(self):
        # Reflect an existing database into a new model
        Base = automap_base()
        # reflect the tables
        Base.prepare(autoload_with=self.engine)      
        # Save reference to the table
        Station = Base.classes.station
        return(Station)
    
    def createMeasurement(self):
        # Reflect an existing database into a new model
        Base = automap_base()
        # reflect the tables
        Base.prepare(autoload_with=self.engine)      
        # Save reference to the table
        Measurement = Base.classes.measurement
        return(Measurement)
    
#######################################################################################
    def queryPrecipitation(self):
        session = Session(self.engine)
        last_12_months_prcp_data= session.query(self.Measurement.date, self.Measurement.prcp)\
                                                .filter(self.Measurement.date >= '2016-08-23')\
                                                .filter(self.Measurement.date <= '2017-08-23')\
                                                .order_by(self.Measurement.date).all()

        # Save the query results as a Pandas DataFrame. Explicitly set the column names
        precipitation_df = pd.DataFrame(last_12_months_prcp_data, columns=['Date','Precipitation'])

        # Sort the dataframe by date
        precipitation_df= precipitation_df.sort_values(by='Date')
        
        # Close the Session
        session.close()
        return(precipitation_df)
    
    def queryStations(self):
        session = Session(self.engine)
        station_list = session.query(self.Station.station).all() 

        # Create the dataframe
        stations_df = pd.DataFrame(station_list, columns=["Station"])

        # Close the Session
        session.close()
        return(stations_df)
    
    def queryTemperature(self):
        session = Session(self.engine)
        temperature_result = session.query(self.Measurement.id, self.Measurement.station, self.Measurement.date, self.Measurement.tobs)\
                                .filter(self.Measurement.date >= '2016-08-23')\
                                .filter(self.Measurement.date <= '2017-08-23')\
                                .filter(self.Measurement.station == "USC00519281").all()
        
        # Save the query results as a Pandas DataFrame. Explicitly set the column names
        temperature_df = pd.DataFrame(temperature_result)

        # Close the Session
        session.close()
        return(temperature_df)
    
    def queryTempstats(self, start):
        session = Session(self.engine)
        temperature_stats = session.query(func.min(self.Measurement.tobs).label('TMIN'),
                            func.max(self.Measurement.tobs).label('TMAX'),
                            func.avg(self.Measurement.tobs).label('TAVG')).filter(self.Measurement.date >= start).all()
        
        # Save the query results as a Pandas DataFrame
        temperature_stats_df = pd.DataFrame(temperature_stats)

        # Close the Session
        session.close()
        return(temperature_stats_df)
    
    def queryTempstats_startend(self, start, end):
        session = Session(self.engine)
        temperature_stats_StartEnd = session.query(func.min(self.Measurement.tobs).label('TMIN'),
                            func.max(self.Measurement.tobs).label('TMAX'),
                            func.avg(self.Measurement.tobs).label('TAVG'))\
                                .filter(self.Measurement.date >= start)\
                                .filter(self.Measurement.date <= end).all()
        
        # Save the query results as a Pandas DataFrame. Explicitly set the column names
        temperature_stats_StartEnd_df = pd.DataFrame(temperature_stats_StartEnd)

        # Close the Session
        session.close()
        return(temperature_stats_StartEnd_df)