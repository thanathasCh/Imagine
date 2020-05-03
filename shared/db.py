import pyodbc
from .model import Event, EventImage, PreprocessedImage
import cv2
import numpy as np
from urllib import request
from passlib.hash import sha256_crypt

class Db:
    def __init__(self):
        self.CONNECTION_STRING = '''Driver={ODBC Driver 17 for SQL Server};
                                    Server=LAPTOP-4QQA0D0G\\SQLEXPRESS;
                                    Database=Imagine;
                                    Trusted_Connection=yes'''
        self.db = pyodbc.connect(self.CONNECTION_STRING)

    def getEvents(self):
        query = '''SELECT EventId, Name as EventName, ImageUrl as CoverImageUrl,
                   Description as Description, OrganizedDateTime as Date
                   FROM Events, Images
                   WHERE EventId = Events.id AND ISCoverImage = 1'''

        cursorSelect = self.db.execute(query)
        fetchQuery = cursorSelect.fetchall()

        data = []
        for i in range(len(fetchQuery)):
            tempEvent = [x for x in fetchQuery[i]]
            data.append(Event(tempEvent[1], tempEvent[3], tempEvent[4],
                              tempEvent[2], eventId=tempEvent[0]))

        cursorSelect.close()
        return data

    def getEventsById(self, id):
        query = f'''SELECT Events.id, Name as EventName, ImageUrl as CoverImageUrl, 
                    Description as Description, OrganizedDateTime as Date
                    FROM Events, Images 
					WHERE Events.id = {id} and Events.id = EventId and IsCoverImage = 1'''
        imageQuery = f'SELECT imageUrl FROM Images WHERE EventId={id}'

        cursorSelect = self.db.execute(query)
        fetchQuery = cursorSelect.fetchone()

        images = []
        cursorSelect = self.db.execute(imageQuery)
        flattenImageUrl = [item for sublist in cursorSelect.fetchall()
                           for item in sublist]
        images.extend(flattenImageUrl)

        event = [x for x in fetchQuery]
        model = EventImage(event[1], event[2], event[3],
                           event[4], images, eventId=event[0])

        cursorSelect.close()
        return model

    def getImgSeqNumber(self, eventId):
        query = f'SELECT COUNT(id) FROM Images where EventId = {eventId} AND IsCoverImage = 0'
        cursorSelect = self.db.execute(query).fetchval()
        return cursorSelect

    def getCoverImgSeqNumber(self, eventId):
        query = f'SELECT COUNT(id) FROM Images where EventId = {eventId} AND IsCoverImage = 1'
        cursorSelect = self.db.execute(query).fetchval()
        return cursorSelect

    def createEvent(self, event: Event):
        query = '''INSERT INTO Events (Name, Description,
                OrganizedDateTime)
                VALUES (?, ?, ?)'''

        cursor = self.db.cursor()
        cursor.execute(query, event.eventName, event.description,
                       event.date)

        self.db.commit()
        return cursor.execute('select @@IDENTITY').fetchval()

    def insertEventImages(self, eventId, imageUrls, coverImageUrl=None):
        query = 'INSERT INTO IMAGES(ImageUrl, EventId, IsCoverImage) VALUES (?, ?, ?)'
        cursor = self.db.cursor()

        cursor.execute(query, coverImageUrl, eventId, 1)
        for url in imageUrls:
            cursor.execute(query, url, eventId, 0)

        self.db.commit()

    def getImageUrl(self, imageId):
        query = f'SELECT ImageUrl FROM Images WHERE id = {imageId}'
        return self.db.execute(query).fetchval()

    def getPreprocessedImages(self, eventId):
        query = f'''SELECT PreprocessedImageUrl
                    FROM Images, PreprocessedImage
                    WHERE EventId = {eventId} and Images.id = PreprocessedImage.ImageId'''

        cursorSelect = self.db.execute(query).fetchall()
        preprocessedImages = []

        for url in cursorSelect:
            reqImage = request.urlopen(url[0])
            img = np.asarray(bytearray(reqImage.read()), dtype="uint8")
            img = cv2.imdecode(img, -1)
            preprocessedImages.append(img)

        cursorSelect.close()
        return preprocessedImages

    def insertPreprocessedImages(self, preprocessedImages):
        query = 'INSERT INTO PreprocessedImage(PreprocessedImageUrl, ImageId) VALUES (?, ?)'
        cursor = self.db.cursor()

        for image in preprocessedImages:
            cursor.execute(query, image.preprocessedImageUrl, image.imageId)

        self.db.commit()

    def isUserNameDuplicated(self, username):
        query = '''SELECT *
                   FROM Users
                   WHERE Users.UserName = ?'''

        cursorSelect = self.db.execute(query, username)
        return len(list(cursorSelect)) > 0

    def login(self, username, password):
        query = '''SELECT Password
                   FROM Users
                   WHERE Users.UserName = ?'''
        
        cursorSelect = self.db.execute(query, username)
        data = list(cursorSelect)

        if not data:
            return False
        else:
            return sha256_crypt.verify(password, data[0][0])        

    def signup(self, firstName, lastName, username, password):
        query = '''INSERT INTO Users 
                   (FirstName, LastName, Username, Password)
                   VALUES
                   (?, ?, ?, ?)'''

        self.db.execute(query, firstName, lastName, username, sha256_crypt.encrypt(password))
        self.db.commit()

    def deleteEvent(self, id):
        query = 'DELETE FROM Events WHERE Id = ?'

        self.db.execute(query, id)
        self.db.commit()