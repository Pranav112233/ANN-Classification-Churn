from flask import Flask

'''
It will create an instans of the Flask class,
which will be your WSGI application
'''

#                Basic Skeleton of Flask while creating our web framework using Flask

## WSGI Application

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course. This should be an  amazing course."

@app.route("/index")
def index():
    return "Welcome to this index page."


if __name__=="__main__":
    app.run(debug=True)