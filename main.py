from flask import Flask, request, render_template, url_for, session, redirect
import os
import urllib
from pathlib import Path
import gc

from shared import messages, flash
from shared.db import Db
from shared.storage import upload_cover_blob, upload_images_blob
from shared.model import Event, EventImage

app = Flask('Imagine')
app.secret_key = "super secret key"

OUTPUT_PATH = 'datasets/img'
BUCKET_NAME = 'eventimagefilter'
db = Db()

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if db.login(username, password):
        flash.success(messages.loginSuccessful)
        session['isLogin'] = True
        session['username'] = username
        session['isAdmin'] = True if username == 'admin' else False
    else:
        flash.danger(messages.loginFailed)
    
    return render_template('main.html')

@app.route('/logout')
def logout():
    session['isLogin'] = False
    session['username'] = ""
    session['isAdmin'] = False

    return render_template('main.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signCheck', methods=['POST'])
def signCheck():
    username = request.form['username']
    password = request.form['password']
    confirmPassword = request.form['confirmPassword']
    firstName = request.form['firstName']
    lastName = request.form['lastName']

    if not username and not password and not firstName and not lastName:
        flash.danger(messages.missingFields)
        return render_template('signup.html')
    elif password != confirmPassword:
        flash.danger(messages.passwordNotMatch)
        return render_template('signup.html')
    elif db.isUserNameDuplicated(username):
        flash.danger(messages.duplicateUsername)
        return render_template('signup.html')
    else:
        db.signup(firstName, lastName, username, password)
        flash.success(messages.signSuccessful)
        return render_template('main.html')
    
@app.route('/event')
def event():
    events = db.getEvents()
    return render_template('event.html', events=events)

@app.route('/addEvent')
def addEvent():
    return render_template('addevent.html')

@app.route('/addEventSubmit', methods=['POST'])
def addEventSubmit():
    if request.method == 'POST':
        name = request.form['eventname']
        description = request.form['description']
        date = request.form['date']
        print(date)
        poster = request.files['posterImage']
        files = request.files.getlist('eventImages')
        
        event = Event(name,description,date)
        eventId = db.createEvent(event)

        imagePath = f'Event/{eventId}/Images'
        coverImagePath = f'Event/{eventId}/CoverImages'
        coverImageUrl = upload_cover_blob(poster, coverImagePath, eventId)
        imageUrls = upload_images_blob(files, imagePath, eventId)

        db.insertEventImages(eventId, imageUrls, coverImageUrl)
    
        events = db.getEvents()       

    flash.info(messages.addEventSuccessful)
    return render_template('event.html', events=events)

@app.route('/selectImage')
def selectImage():
    return render_template('selectimage.html')

@app.route('/processImage', methods = ['POST'])
def processImage():
    root_dir = Path('./datasets')
    items = root_dir.iterdir()
    
    for file in items:
        if file.is_file():
            os.remove(file)

    if request.form.getlist('userImage[]'):
        images = request.form.getlist('userImage[]')
        for i in range(len(images)):
            response = urllib.request.urlopen(images[i])
            with open(OUTPUT_PATH + str(i) + '.jpg', 'wb') as f:
                f.write(response.file.read())
    else:
        flash.danger(messages.fileOrImageMissing)
    
    return render_template('processImage.html')

@app.route('/eventDetail/<int:id>')
def eventDetail(id):
    event = db.getEventsById(id)
    return render_template('eventdetail.html', model=event)

@app.route('/editEvent/<int:id>')
def editEvent(id):
    event = db.getEventsById(id)
    return render_template('editevent.html', model=event)

@app.route('/editEventSubmit', methods=['POST'])
def editEventSubmit():
    return redirect(url_for('event'))

@app.route('/deleteEvent/<int:id>')
def deleteEvent(id):
    db.deleteEvent(id)
    return redirect(url_for('event'))

@app.route('/ImageFilter')
def imageFilter():
    return render_template('imageFilter.html')

def returnResult():
    pass

@app.errorhandler(404)
def page_not_found(e):
    return messages.error404

@app.errorhandler(500)
def internal_error(e):
    return messages.error505

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(debug=True)