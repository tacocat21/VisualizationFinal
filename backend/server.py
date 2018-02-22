import flask

app = flask.Flask(__name__)

@app.route("/")
def main():
    return "Hello!"

@app.route("/api/")
def get_all():
    pass