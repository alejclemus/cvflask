# app.py
from flask import Flask, request, render_template           # import flask
import os,optparse 
import yaml
app = Flask(__name__)             # create an app instance
app.static_folder = 'Templates'

data = yaml.load(open('info.yml'))
environment=os.getenv("ENVIRONMENT","development")

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return render_template('index.html', data = data)         # which returns "hello world"

@app.route("/information")
def info():
    return "test1"

@app.route("/academics")
def academics():
    return "test2"

@app.route("/experience")
def experience():
    return "test3"

if __name__ == "__main__":        # on running python app.py
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug) # run the flask app
