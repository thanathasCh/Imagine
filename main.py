from flask import Flask, request, render_template, url_for
import numpy as np
import data
import messages
import flash
import os
from werkzeug.utils import secure_filename
import urllib

app = Flask('Imagine')

OUTPUT_PATH = 'datasets/img.jpg'
@app.route('/')
def index():
    return render_template('main.html')

# Login Page
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin':
        flash.success(messages.loginSuccessful)
    else:
        flash.danger(messages.loginSuccessful)
    
    return render_template('main.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signCheck', methods=['POST'])
def signCheck():
    username = request.form['username']
    password = request.form['password']
    firstName = request.form['firstName']
    lastName = request.form['lastName']

    flash.success(messages.signSuccessful)
    return render_template('main.html')
    
# end

# Event Page
@app.route('/event')
def event():
    return render_template('event.html', events=data.events)

@app.route('/addEvent')
def addEvent():
    return render_template('addevent.html')

@app.route('/addEventSubmit', methods=['POST'])
def addEventSubmit():
    if request.method == 'POST':
        name = request.form['eventname']
        description = request.form['description']
        date = request.form['date']
        poster = request.files['posterImage']
        files = request.files.getlist('eventImages')
        
        model = {
            'id': len(data.events),
            'eventName': name,
            'description': description,
            'date': date
        }
        
        # data.events.append(model)
       
        # if request.files:
        #     print(request.files['eventImages'])
        #     return 'done'
        # return('halfly done')
            

    flash.info(messages.addEventSuccessful)
    return render_template('event.html', events=data.events)

@app.route('/selectImage')
def selectImage():
    return render_template('selectimage.html')

@app.route('/processImage', methods = ['POST'])
def processImage():
    try:
        image = request.form['userImage']
        response = urllib.request.urlopen(image)
        with open(OUTPUT_PATH, 'wb') as f:
            f.write(response.file.read())
    except:
        image = request.files['userImage']
        image.save(OUTPUT_PATH)
    
    return render_template('processImage.html')

@app.route('/eventDetail/<int:id>')
def eventDetail(id):
    return render_template('eventdetail.html', model=data.events[id-1])

@app.route('/editEvent/<int:id>')
def editEvent(id):
    return render_template('editevent.html', model=data.events[id-1])

@app.route('/deleteEvent/<int:id>')
def deleteEvent(id):
    del data.events[id-1]
    flash.success(messages.deleteSuccessful)
    return render_template('event.html', events=data.events)
# end

# Image Filter Page
@app.route('/ImageFilter')
def imageFilter():
    return render_template('imageFilter.html')

def returnResult():
    pass
# end

# Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return messages.error404

@app.errorhandler(500)
def internal_error(e):
    return messages.error505
# end


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(debug=True)