## Instructions
1. Clone repository
2. Create a new virtual environment using Python 3.4
3. Activate your virtual environment `source virt_env_path/bin/activate`
4. By the terminal navigate to the clone rope and dnstall requirements.txt
5. In terminal/console run `python app.py `. Run the service on port 5000.
6. Test the Web API with the following url: http://127.0.0.1:5000/regions 
7. You should get the following json:
```
{
    regions: [
        "England",
        "Scotland",
        "UK",
        "Wales"
    ]
}
```

# Working project

If you want to have a try of this project you can access to the following Enp Points:
1. Endpoint that returns a list of regions (Every time you call this endpoint the databes is updated with https://www.metoffice.gov.uk/ data): https://uk-climate-api.herokuapp.com/
1. Endpoint that returns the list of years stored in db: https://uk-climate-api.herokuapp.com/years
1. Endpoint that returns the list of conditions in the DB: https://uk-climate-api.herokuapp.com/conditions
1.  Endpoint that returns all Climate conditions for all the regions for an specific year and condition: https://uk-climate-api.herokuapp.com/compare/`<string:year>/<string:condition>`
1. Endpoint that returns Min, Max and Mean Temperature for an specific region and year: https://uk-climate-api.herokuapp.com/temperature/`<string:region>/<string:year>`