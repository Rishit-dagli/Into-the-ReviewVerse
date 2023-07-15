# how to use css in python_ flask
# flask render_template example
 
from flask import Flask, render_template
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templates', static_folder='static')
 
# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug = True)