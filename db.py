import pyodbc

class DB:
    def __init__(self):
        self.CONNECTION_STRING = """Driver={ODBC Driver 17 for SQL Server};
                                    Server=35.187.239.143;
                                    Database=Imagine;
                                    UID=sqlserver;
                                    PWD=alexanderthegreat;"""
        self.db = pyodbc.connect(self.CONNECTION_STRING)


dbc = DB()
# a = """SELECT  Events.id, Name as eventName, CoverImageUrl as imageUrl, 
#        Description as description, OrganizedDateTime as date, imageUrl
#        FROM Events,Images WHERE Images.EventId = Events.id"""

a = """SELECT  Events.id, Name as eventName, CoverImageUrl as imageUrl, 
       Description as description, OrganizedDateTime as date
       FROM Events"""
cursor = dbc.db.cursor()

cursorSelect = cursor.execute(a)
columns = [column[0] for column in cursorSelect.description]
columns.append("imageUrl")
print(columns)
print()
fetchQuery = cursorSelect.fetchall()
eventIdLists = [column[0] for column in fetchQuery]
imageLists = []

for i in eventIdLists:
    query = f"""SELECT imageUrl FROM Images WHERE EventId={i}"""
    cursorSelect = dbc.db.execute(query)
    # imageLists.append(list(cursorSelect.fetchall()))
    abc = cursorSelect.fetchall()
    flattened = [item for sublist in abc for item in sublist]
    imageLists.append(flattened)
print(imageLists)
print('--------------------')

# data = []
data = {}
sss = 0
for i in range(len(fetchQuery)):
    testSingleList = [x for x in fetchQuery[i]]
    testSingleList.append(imageLists[i])
    # data.append(dict(zip(columns,testSingleList)))
    data[sss] = dict((zip(columns,testSingleList)))
    sss += 1

print()
print(data)

# results = []
# for row in test:
#     # print(type(row))
    
    # results.append(dict(zip(columns, row)))
#     print(row)
#     print()

# print('aaaa',results)

# # b = dbc.db.execute(a)
# # data = [x for x in b]
# # print(data)
# # results = cursor.execute(a).fetchall()
# # .fetchone()

# # print(cursor.description)
# # i = 0
# # for row in result:
# #     for a in row:
# #         print(f'{cursor.description[i][0]}= {a}')
# #         i +=1
# #     i = 0
