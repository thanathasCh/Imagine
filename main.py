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
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f'{username} {password}'
    
# end

# Event Page
@app.route('/event')
def event():
    events = [
                {
                    'id': 0,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                },
                {
                    'id': 0,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                },
                {
                    'id': 0,
                    'eventName': 'Au Freshy Day and Night',
                    'imageUrl': 'https://www.abactoday.com/wp-content/uploads/2015/08/uc59282e7be59f20b867d53511131956f-1_14401580346861.jpg',
                    'description': 'Bla Bla Bla Bla'
                }
            ]
            
    return render_template('event.html', events=events)

@app.route('/addEvent')
def addEvent():
    return render_template('addevent.html')

@app.route('/eventDetail/<int:id>')
def eventDetail(id):
    return 'Event Detail'

@app.route('/editEvent/<int:id>')
def editEvent(id):
    return 'Edit Event'

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

@app.errorhandler(500)
def internal_error(e):
    return 'Internal Error is occured'
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