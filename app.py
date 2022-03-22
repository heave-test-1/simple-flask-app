from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    headers = flask.request.headers
    return "Request headers:\n" + str(headers)

app.run(host="0.0.0.0", port=8080)

