# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance
import os,optparse

developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug) # run the flask app
