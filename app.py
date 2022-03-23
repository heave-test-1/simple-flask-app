from flask import Flask
from flask import request


app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    headers = request.headers
    print("Got request")
    print("Request headers:\n" + str(headers))
    return "Request headers:\n" + str(headers)

app.run(host="0.0.0.0", port=8080)
