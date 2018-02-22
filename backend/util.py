import json
import os

UN_ORIGINAL_DATA_FILENAME = os.path.join(os.path.dirname(__file__), "data",
                                         "UN_MigrantStockByOriginAndDestination_2017.xlsx")
IMMIGRATION_REGION_DATA_FILENAME = os.path.join(os.path.dirname(__file__), "data", "immigration_region_result.json")
IMMIGRATION_COUNTRY_DATA_FILENAME = os.path.join(os.path.dirname(__file__), "data", "immigration_country_result.json")
EMIGRATION_REGION_DATA_FILENAME = os.path.join(os.path.dirname(__file__), "data", "emigration_region_result.json")
EMIGRATION_COUNTRY_DATA_FILENAME = os.path.join(os.path.dirname(__file__), "data", "emigration_country_result.json")

def load_json(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

def save_json(data, filename):
    with open(filename, 'w') as fp:
        json.dump(data, fp)