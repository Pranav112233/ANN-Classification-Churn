## Integrating HTML File with Web App
from flask import Flask, render_template
#  render_template -> Responsible for re-directing to the HTML page 
'''
It will create an instans of the Flask class,
which will be your WSGI application
'''

#                Basic Skeleton of Flask while creating our web framework using Flask

## WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1> Welcome to this Flask course</H1></html>"

@app.route("/index")
def index():
    return render_template('index1.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)