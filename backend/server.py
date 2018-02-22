import flask
import util

app = flask.Flask(__name__)
immigration_region_result = util.load_json(util.IMMIGRATION_REGION_DATA_FILENAME)
immigration_country_result = util.load_json(util.IMMIGRATION_COUNTRY_DATA_FILENAME)
emigration_region_result = util.load_json(util.EMIGRATION_REGION_DATA_FILENAME)
emigration_country_result = util.load_json(util.EMIGRATION_COUNTRY_DATA_FILENAME)

@app.route("/")
def main():
    return "Hello!"

@app.route("/api/country/immigration")
def get_country_immigration():
    return flask.jsonify(immigration_country_result)

@app.route("/api/region/immigration")
def get_region_immigration():
    return flask.jsonify(immigration_region_result)

@app.route("/api/country/emigration")
def get_country_emigration():
    return flask.jsonify(emigration_country_result)

@app.route("/api/region/emigration")
def get_region_emigration():
    return flask.jsonify(emigration_region_result)

