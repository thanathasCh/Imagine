from flask import Flask, request, render_template, url_for, session, redirect
import os
import urllib
from pathlib import Path
import gc
import numpy as np
from copy import deepcopy
import face_recognition
import cv2

from shared import messages, flash
from shared.db import Db
from shared.storage import Storage
from shared.model import Event, EventImage

app = Flask('Imagine')
app.secret_key = "super secret key"

OUTPUT_PATH = 'datasets'
BUCKET_NAME = 'eventimagefilter'
MODEL = 'hog'
db = Db()
storage = Storage()

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
        poster = request.files['posterImage']
        files = request.files.getlist('eventImages')
        secondFiles = request.files.getlist('secondEventImages')

        event = Event(name, description, date)
        eventId = db.createEvent(event)

        seq_cover_number = db.getCoverImgSeqNumber(eventId) + 1
        coverImageUrl = storage.upload_cover_blob(poster, eventId, seq_cover_number)

        seq_number = db.getImgSeqNumber(eventId)
        imageUrls = storage.upload_images_blob(files, eventId, seq_number)
        imageIds = db.insertEventImages(eventId, imageUrls, coverImageUrl)

        for s, i in zip(secondFiles, imageIds):
            file_read = s.read()
            npImg = np.fromstring(file_read, np.uint8)
            img = cv2.imdecode(npImg, cv2.IMREAD_UNCHANGED)
            locations = face_recognition.face_locations(img, model=MODEL)
            encoding = face_recognition.face_encodings(img, locations)
            db.insertPreprocessedImages(encoding, i[0][0])

        flash.success(messages.addEventSuccessful)
        return redirect(url_for('event'))
    else:
        flash.danger(messages.unableToCreateEvent)
        return render_template('addevent.html')
        
@app.route('/selectImage')
def selectImage():
    return render_template('selectimage.html')

@app.route('/processImage', methods = ['POST'])
def processImage():
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
    flash.success(messages.deleteSuccessful)
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
