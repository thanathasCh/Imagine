import pyodbc

class Db:
    def __init__(self):
        self.CONNECTION_STRING = """Driver={ODBC Driver 17 for SQL Server};
                                    Server=35.187.239.143;
                                    Database=Imagine;
                                    UID=sqlserver;
                                    PWD=alexanderthegreat;"""
        self.db = pyodbc.connect(self.CONNECTION_STRING)

    def getEvents(self):
        query = """SELECT id, Name as eventName, CoverImageUrl as CoverimageUrl, 
                    Description as description, OrganizedDateTime as date
                    FROM Events """
        
        cursorSelect = self.db.execute(query)
        # construct list of column names       
        columnNames = [column[0] for column in cursorSelect.description]
        fetchQuery = cursorSelect.fetchall()
        
        data = []
        for i in range(len(fetchQuery)):
            tempEvent = [x for x in fetchQuery[i]]
            data.append(dict((zip(columnNames, tempEvent))))

        cursorSelect.close()
        return data

    def getEventsById(self, id):
        query = f"""SELECT id, Name as eventName, CoverImageUrl as imageUrls, 
                    Description as description, OrganizedDateTime as date
                    FROM Events WHERE id = {id}"""
        imageQuery = f"""SELECT imageUrl FROM Images WHERE EventId={id}"""

        cursorSelect = self.db.execute(query)

        # construct list of column names       
        columnNames = [column[0] for column in cursorSelect.description]
        columnNames.append("imageUrls")
        
        fetchQuery = cursorSelect.fetchone()

        imageLists = []
        cursorSelect = self.db.execute(imageQuery)
        flattenImageUrl = [item for sublist in cursorSelect.fetchall() for item in sublist]
        imageLists.extend(flattenImageUrl)

        event = [x for x in fetchQuery]
        event.append(imageLists)
        data = dict((zip(columnNames, event)))

        cursorSelect.close()
        return data

