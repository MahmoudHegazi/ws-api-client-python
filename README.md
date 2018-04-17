# ws-api-client-python
The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/driveate/ws-api-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/driveate/ws-api-client-python.git`)

Then import the package:
```python
import ws_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ws_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

from __future__ import print_function
import time
import ws_api_client
from ws_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user_key
ws_api_client.configuration.default_config.api_key['user_key'] = 'YOUR_API_KEY'
# create an instance of the API class
api_instance = ws_api_client.MakesApi()
countries = 'us,gb,jp' # str | Show information for local manufacturers from specified countries only. Use `GET /countries/` method to get the full list of countries. (e.g. `us,gb,jp`) (optional)
try:
    # Get list of manufacturers
    api_response = api_instance.makes_list(countries=countries)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MakesApi->makes_list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wheel-size.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BoltPatternsApi* | [**bolt_patterns_list**](docs/BoltPatternsApi.md#bolt_patterns_list) | **GET** /bolt-patterns/ | Get list of bolt patterns
*BoltPatternsApi* | [**bolt_patterns_read**](docs/BoltPatternsApi.md#bolt_patterns_read) | **GET** /bolt-patterns/{bolt_pattern}/ | Model modifications by bolt pattern
*CountriesApi* | [**countries_list**](docs/CountriesApi.md#countries_list) | **GET** /countries/ | Returns a list of countries
*GenerationsApi* | [**generations_list**](docs/GenerationsApi.md#generations_list) | **GET** /generations/ | Generations for the given model
*MakesApi* | [**makes_list**](docs/MakesApi.md#makes_list) | **GET** /makes/ | Returns a list of manufacturers
*MarketsApi* | [**markets_list**](docs/MarketsApi.md#markets_list) | **GET** /markets/ | Returns a list of markets/regions
*ModelsApi* | [**models_list**](docs/ModelsApi.md#models_list) | **GET** /models/ | Returns a list of models by manufacturer
*ModelsApi* | [**models_read**](docs/ModelsApi.md#models_read) | **GET** /models/{make}/{slug}/ | Get more info about model
*ModelsApi* | [**models_read_year**](docs/ModelsApi.md#models_read_year) | **GET** /models/{make}/{slug}/{year}/ | Get more info about model/year
*SearchApi* | [**search_by_hf_tire_list**](docs/SearchApi.md#search_by_hf_tire_list) | **GET** /search/by_hf_tire/ | Find models matching given high flotation tire
*SearchApi* | [**search_by_model_list**](docs/SearchApi.md#search_by_model_list) | **GET** /search/by_model/ | Find OE and option fitments by model/year/trim
*SearchApi* | [**search_by_rim_list**](docs/SearchApi.md#search_by_rim_list) | **GET** /search/by_rim/ | Find models matching given rim parameters
*SearchApi* | [**search_by_tire_list**](docs/SearchApi.md#search_by_tire_list) | **GET** /search/by_tire/ | Find models matching given tire parameters
*TiresApi* | [**tires_list**](docs/TiresApi.md#tires_list) | **GET** /tires/ | Returns a list of tires
*TiresApi* | [**tires_read**](docs/TiresApi.md#tires_read) | **GET** /tires/{tire}/ | Model modifications matching given tire
*TrimsApi* | [**trims_list**](docs/TrimsApi.md#trims_list) | **GET** /trims/ | Model modifications
*VehiclesApi* | [**vehicles_list**](docs/VehiclesApi.md#vehicles_list) | **GET** /vehicles/ | Find OE and option fitments by model/year/trim
*YearsApi* | [**years_list**](docs/YearsApi.md#years_list) | **GET** /years/ | Returns list of years for the given manufacturer/model


## Documentation For Models

 - [Aggregation](docs/Aggregation.md)
 - [Body](docs/Body.md)
 - [BoltPattern](docs/BoltPattern.md)
 - [Country](docs/Country.md)
 - [Generation](docs/Generation.md)
 - [Make](docs/Make.md)
 - [MakeWithModels](docs/MakeWithModels.md)
 - [Market](docs/Market.md)
 - [Model](docs/Model.md)
 - [ModelWithTires](docs/ModelWithTires.md)
 - [ModelWithTrims](docs/ModelWithTrims.md)
 - [Power](docs/Power.md)
 - [Pressure](docs/Pressure.md)
 - [RimAgregation](docs/RimAgregation.md)
 - [SizeAggregation](docs/SizeAggregation.md)
 - [Tire](docs/Tire.md)
 - [TiresAggregation](docs/TiresAggregation.md)
 - [Trim](docs/Trim.md)
 - [TrimWithMarketAndYears](docs/TrimWithMarketAndYears.md)
 - [Vehicle](docs/Vehicle.md)
 - [Wheel](docs/Wheel.md)
 - [WheelPair](docs/WheelPair.md)
 - [Year](docs/Year.md)


## Documentation For Authorization


## user_key

- **Type**: API key
- **API key parameter name**: user_key
- **Location**: URL query string


## Author

info@wheel-size.com

