import pyodbc

class Db:
    def __init__(self):
        self.CONNECTION_STRING = """Driver={ODBC Driver 17 for SQL Server};
                                    Server=35.187.239.143;
                                    Database=Imagine;
                                    UID=sqlserver;
                                    PWD=alexanderthegreat;"""
        self.db = pyodbc.connect(self.CONNECTION_STRING)

    def getEvents(self, id=None):
        query = """SELECT id, Name as eventName, CoverImageUrl as imageUrl, 
                    Description as description, OrganizedDateTime as date
                    FROM Events """
        if (id is not None): query += f"WHERE id = {id}"
        
        cursor = self.db.cursor()
        cursorSelect = cursor.execute(query)

        # construct list of column names       
        columnNames = [column[0] for column in cursorSelect.description]
        columnNames.append("imageUrl")
        fetchQuery = cursorSelect.fetchall()
        
        eventIdLists = [column[0] for column in fetchQuery] # construct list of eventId
        imageLists = []
        # query imageUrl for each event
        for i in eventIdLists:
            imageQuery = f"""SELECT imageUrl FROM Images WHERE EventId={i}"""
            cursorSelect = dbc.db.execute(imageQuery)
            flattenImageUrl = [item for sublist in cursorSelect.fetchall() for item in sublist]
            imageLists.append(flattenImageUrl)

        data = {}
        for i in range(len(fetchQuery)):
            tempEvent = [x for x in fetchQuery[i]]
            tempEvent.append(imageLists[i])
            data[eventIdLists[i]] = dict((zip(columnNames, tempEvent)))

        cursor.close()
        return data

dbc = Db()
dbc.getEvents(1)

