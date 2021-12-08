import requests
import json

URL="http://127.0.0.1:8000/studetail/"

def getdata(id = None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL, data=json_data)
    data=r.json()
#     print(data)

def postdata():
    data={
        'name':'Ramiz',
        'roll':15,
        'city':'Indore'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

# postdata()

def deletedata():
    data={'id':3}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
deletedata()

def updatedata():
    data={'id':3,
    'name':'Sanvi'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

# updatedata()