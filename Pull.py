import requests
import json
import pyodbc
server = 'localhost'
database = 'python'
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                      "Server=" + server + ";" +
                      "Database=" + database + ";" +
                      "Trusted_Connection=yes;")
cursor = conn.cursor()
CheckT = "SELECT * FROM information_schema.tables where table_name = 'jsonAPI';"
DropT = "Drop table jsonAPI"
conn.execute(CheckT)
flag = conn.execute(CheckT).fetchall()
if flag:
    conn.execute(DropT)
    conn.commit()
CreateT = "Create table jsonAPI(userid nvarchar(100),id nvarchar(100),title nvarchar(500),completed nvarchar(100));"
conn.execute(CreateT)
conn.commit()
for i in range(1,10):
    url = "https://jsonplaceholder.typicode.com/todos/" + str(i)
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    """print(json.dumps(parsed, indent=4))
    print(parsed["id"])
    insertT = "Insert into jsonAPI(userid,id,title,completed) values(" + str(parsed["userId"]) + str(parsed["id"]) + str(parsed["title"]) + str(parsed["completed"]) + ");"
    """
    insertT = "Insert into jsonAPI(userid,id,title,completed) values(?,?,?,?);"
    conn.execute(insertT,(str(parsed["userId"]) , str(parsed["id"]) , str(parsed["title"]) , str(parsed["completed"])))
    conn.commit()

