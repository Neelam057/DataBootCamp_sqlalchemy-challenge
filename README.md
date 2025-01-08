# Climate Analysis for Honolulu, Hawaii

This project analyzes the climate data of Honolulu, Hawaii, to assist in planning a vacation. The analysis focuses on weather-related data, including precipitation, temperature, and station data. The project uses Python, Flask, SQLAlchemy, and Jupyter Notebook to handle and visualize the data.


## Project Overview

The goal of this project is to perform a climate analysis using weather data for Honolulu. This analysis includes queries on precipitation, temperature observations, and station data, and visualizations of precipitation trends and temperature distribution.

The project involves:
- Connecting to a SQLite database using SQLAlchemy.
- Reflecting tables in the database to Python classes.
- Performing SQL queries to extract weather statistics and trends.
- Building a Flask API to serve data and display climate information.
- Implementing various routes for dynamic and static queries.

## Technologies Used

- **Python**: Primary programming language used for the project.
- **Flask**: Web framework used to build the API.
- **SQLAlchemy**: ORM used to interact with the SQLite database.
- **SQLite**: The database used to store the weather data.
- **Pandas**: Data manipulation and analysis library.
- **Matplotlib**: Used for plotting precipitation bar chart and temperature histogram.
- **Jupyter Notebook**: For running and testing queries and performing data analysis.

## Project Structure

The project is organized as follows:

```
climate data/
├── Resources/                  
│   ├── hawaii.sqlite
│   ├── hawaii.measurements.csv
│   ├── hawaii.stations.csv 
├── app.py                
├── sql_helper.py                     
├── climate_starter.ipynb 
└── README.md 
```           

### Running Jupyter Notebook
To start performing climate analysis, open the `notebook.ipynb` in a Jupyter Notebook interface. This notebook contains steps for querying and visualizing the climate data.

### Running the Flask API
The Flask API provides the following routes to access the data:

1. **Precipitation Analysis**:
   - Route: `/api/v1.0/precipitation`
   - Returns the precipitation data for the last year.

2. **Station Data**:
   - Route: `/api/v1.0/stations`
   - Returns data for all stations in the database.

3. **Temperature Observations**:
   - Route: `/api/v1.0/tobs`
   - Returns temperature observations for the most active station (USC00519281) for the last year.

4. **Start Date Analysis**:
   - Route: `/api/v1.0/<start>`
   - Returns the minimum, maximum, and average temperature from the start date to the most recent date in the dataset.

5. **Start and End Date Analysis**:
   - Route: `/api/v1.0/<start>/<end>`
   - Returns the minimum, maximum, and average temperature between the specified start and end dates.

