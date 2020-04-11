import pyodbc
from model import Event, EventImage
import datetime

class Db:
    def __init__(self):
        self.CONNECTION_STRING = """Driver={ODBC Driver 17 for SQL Server};
                                    Server=35.187.239.143;
                                    Database=Imagine;
                                    UID=sqlserver;
                                    PWD=alexanderthegreat;"""
        self.db = pyodbc.connect(self.CONNECTION_STRING)

    def getEvents(self):
        query = """SELECT id, Name as EventName, CoverImageUrl as CoverimageUrl, 
                    Description as Description, OrganizedDateTime as Date
                    FROM Events """

        cursorSelect = self.db.execute(query)
        fetchQuery = cursorSelect.fetchall()

        data = []
        for i in range(len(fetchQuery)):
            tempEvent = [x for x in fetchQuery[i]]
            data.append(Event(tempEvent[1], tempEvent[2], tempEvent[3],
                              tempEvent[4], eventId=tempEvent[0]))

        cursorSelect.close()
        return data

    def getEventsById(self, id):
        query = f"""SELECT id, Name as EventName, CoverImageUrl as CoverImageUrl, 
                    Description as Description, OrganizedDateTime as Date
                    FROM Events WHERE id = {id}"""
        imageQuery = f"""SELECT imageUrl FROM Images WHERE EventId={id}"""

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

    def getSeqNumber(self, eventId):
        query = f'''SELECT COUNT(id) FROM Images where EventId = {eventId}'''
        cursorSelect = self.db.execute(query).fetchval()
        return cursorSelect

    def createEvent(self, event: Event):
        query = '''INSERT INTO Events (Name, Description,
                OrganizedDateTime, CoverImageUrl)
                VALUES (?, ?, ?, ?)'''

        cursor = self.db.cursor()
        cursor.execute(query, event.eventName, event.description,
                       event.date, event.coverImageUrl)

        self.db.commit()
        return cursor.execute('select @@IDENTITY').fetchval()

    def insertEventImage(self, eventId, imageUrls):
        query = 'INSERT INTO IMAGES(ImageUrl, EventId) VALUES (?, ?)'
        cursor = self.db.cursor()
        for url in imageUrls:
            cursor.execute(query, url, eventId)
        self.db.commit()


