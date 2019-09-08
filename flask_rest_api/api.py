from flask import Flask
from flask_restful import Resource, Api
import json

# Open countries captial json data file
with open("data_file.json", "r") as capitals:
    data = json.load(capitals)

# create a instance of Flask
app = Flask(__name__)
# create a instance of flask_restful using Flask app
api = Api(app)

# Create a recourse c
class Country(Resource):
    # define a get request
    def get(self,country_id):
        ''' Sends back the capital city of the country id'''

        country_id = country_id.strip().capitalize() 
        
        # create a json response
        response =  {'country': country_id}
        
        # if country_id is valid send the capital else send 'NOT FOUND'
        if country_id in data:
            response['capital'] = data[country_id]
        else :
            response['capital'] = "NOT FOUND" 
        
        return response 

# register the resource route to the flask_restful
api.add_resource(Country, '/<string:country_id>')

if __name__ == '__main__':
    app.run(debug=True)