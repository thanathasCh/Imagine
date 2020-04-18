from flask import Flask, request, render_template, url_for
# import numpy as np
import data
import messages
import flash
import os
from db import Db
import urllib
from pathlib import Path

# import storage
from storage import upload_cover_blob, upload_images_blob
from model import Event, EventImage

app = Flask('Imagine')
app.secret_key = "super secret key"

OUTPUT_PATH = 'datasets/img'
BUCKET_NAME = 'eventimagefilter'

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
    events = Db().getEvents()
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

        imagePath = f'''Event/{name}/Images'''
        coverImagePath = f'''Event/{name}/CoverImages'''
        coverImageUrl = upload_cover_blob(BUCKET_NAME, poster, coverImagePath)
        event = Event(name,coverImageUrl,description,date)
        eventId = Db().createEvent(event)
        imageUrls = upload_images_blob(BUCKET_NAME, files, imagePath,eventId)
        Db().insertEventImage(eventId,imageUrls)
    
        events = Db().getEvents()       

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
    event = Db().getEventsById(id)
    return render_template('eventdetail.html', model=event)

@app.route('/editEvent/<int:id>')
def editEvent(id):
    event = Db().getEventsById(id)
    return render_template('editevent.html', model=event)

@app.route('/deleteEvent/<int:id>')
def deleteEvent(id):
    event = Db().getEventsById(id)
    return render_template('event.html', events=event)
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