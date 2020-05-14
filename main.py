from flask import Flask, request, render_template, url_for, session, redirect
import os
from urllib.request import urlopen
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
from shared.jsonNp import npToJson, jsonToNp, convertBinaryToImage

app = Flask('Imagine')
app.secret_key = "super secret key"

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
    return render_template('addevent.html', model=Event())

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
            img = convertBinaryToImage(s.read())
            locations = face_recognition.face_locations(img, model=MODEL)
            encoding = face_recognition.face_encodings(img, locations)
            db.insertPreprocessedImages(encoding, i[0][0])

        flash.success(messages.addEventSuccessful)
        return redirect(url_for('event'))
    else:
        flash.danger(messages.unableToCreateEvent)
        return render_template('addevent.html')
        
@app.route('/selectImage/<int:id>')
def selectImage(id):
    return render_template('selectimage.html', eventId = id)

@app.route('/processImage', methods = ['POST'])
def processImage():
    files = request.form.getlist('userImages[]')
    eventId = request.form['eventId']
    similarity = int(request.form['similarity'])
    TOLERANCE = 1 - (similarity / 100)

    if not files:
        flash.danger(messages.fileOrImageMissing)
        return redirect(url_for('selectImage', id=eventId))

    known = []
    imageIds = set()

    for f in files:
        img = cv2.imdecode(np.fromstring(urlopen(f).file.read(), np.uint8), 1)
        locations = face_recognition.face_locations(img, model=MODEL)
        encoding = face_recognition.face_encodings(img, locations)
        known = known + encoding
    
    unknown = db.getPreprocessedImages(eventId)
    for face, imageId in unknown:
        results = face_recognition.compare_faces(known, face, TOLERANCE)
        if True in results:
            imageIds.add(imageId)

    if imageIds:
        event = db.getEventInformation(eventId)
        eventImages = db.getImageByIds(imageIds)
        return render_template('showImages.html', event = event, eventImages = eventImages)
    else:
        # flash.info(messages.noMatchFace)
        # return redirect(url_for('selectImage', id=eventId))
        return ""

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
    if request.method == 'POST':
        id = request.form['eventId']
        name = request.form['eventname']
        description = request.form['description']
        date = request.form['date']
        event = Event(name, description, date, eventId=id)
        # poster = request.files['posterImage']
        # files = request.files.getlist('eventImages')
        # secondFiles = request.files.getlist('secondEventImages')
        db.updateEvent(event)

        flash.success(messages.editEventSuccessful)
    else:
        flash.danger(messages.unableToEditEvent)
    
    return redirect(url_for('event'))

@app.route('/deleteEvent/<int:id>')
def deleteEvent(id):
    db.deleteEvent(id)
    storage.deleteImagesByEventId(id)
    flash.success(messages.deleteSuccessful)
    return redirect(url_for('event'))

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