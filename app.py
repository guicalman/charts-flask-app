from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from services import RegionList, RegionCompare, TemperatureList, YearList, ConditionList
from load_data import load_all_data

# Exceutes the method that populate the database
load_all_data()

if __name__ == '__main__':
    # Configures the Climate Backend endpoints
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    # Endpoint that returns a list of regions
    api.add_resource(RegionList, '/')
    # Endpoint that returns the list of years stored in db
    api.add_resource(YearList, '/years')
    # Endpoint that returns a json with all the Climate conditions all the regions in an
    # specicif year and specific condition
    api.add_resource(RegionCompare, '/compare/<string:year>/<string:condition>')
    # Endpoint that returns Min, Max and Mean Temperature for a specific region in a year
    api.add_resource(TemperatureList, '/temperature/<string:region>/<string:year>')
    #Endpoint the returns the list of conditions in the DB
    api.add_resource(ConditionList, '/conditions')
    app.run(port=5000, debug=True)