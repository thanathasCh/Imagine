from flask import Flask, request, render_template, url_for
import numpy as np

app = Flask('Imagine')


@app.route('/')
def index():
    return render_template('main/index.html')

# Login Page
def login():
    pass
# end

# Event Page
@app.route('/event')
def event():
    return render_template('event/index.html')

def addEvent():
    pass

def editEvent():
    pass

def deleteEvent():
    pass
# end

# Event Image Page
def eventImage():
    pass

def addEventImage():
    pass

def deleteEventImage():
    pass
# end

# Image Filter Page
def imageFilter():
    pass

def updateImage():
    pass

def returnResult():
    pass

'''
@app.route('/test/<string:user>')
def test(user):
    pass
'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)