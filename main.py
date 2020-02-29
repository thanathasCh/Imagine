from flask import Flask, request, render_template, url_for, flash
import numpy as np

app = Flask('Imagine')
'''
    flash: info, danger, warning, success
'''

@app.route('/')
def index():
    return render_template('main.html')

# Login Page
@app.route('/login')
def login():
    return render_template('main.html')
    
# end

# Event Page
@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/addEvent')
def addEvent():
    return render_template('addevent.html')

@app.route('/eventdetail')
def eventDetail():
    return 'Event Detail'

def editEvent():
    pass

def deleteEvent():
    pass

def addEventImage():
    pass

def deleteEventImage():
    pass
# end

# Image Filter Page
def imageFilter():
    pass

def uploadImage():
    pass

def returnResult():
    pass
# end

# Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return 'This page is not finished yet! GO BACK!!'
# end

'''
@app.route('/test/<string:user>')
def test(user):
    pass
'''


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()