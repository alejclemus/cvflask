# app.py
from flask import Flask, request, render_template           # import flask
import os,optparse 
import yaml
app = Flask(__name__)             # create an app instance
app.static_folder = 'Templates'
environment=os.getenv("ENVIRONMENT","development")
with open("Templates/info.yml", 'r',encoding='utf-8') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        
@app.route("/")                   # at the end point /
def main():                      
    return render_template('index.html', data = data)        

@app.route("/info")                   # at the end point /
def info():                      
    return render_template('index.html', data = data)        

@app.route("/formacion")
def academics():
    return render_template('formacion.html', data = data)

@app.route("/experiencia")
def experience():
    return render_template('experiencia.html', data = data)

if __name__ == "__main__":        # on running python app.py
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug) # run the flask app
