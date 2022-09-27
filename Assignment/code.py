from pymongo import MongoClient
import pandas as pd

localConn=None
def getConnection():
    try:
        global localConn
        localConn = MongoClient("mongodb://localhost:27017",connect=False)

    except Exception as e:
        print(str(e))

def solution():
    getConnection()
    data=pd.read_json('data.json')
    data=data.to_dict(orient="records")
    db=localConn['Employees']
    if 'details' not in db.list_collection_names():
        db.details.insert_many(data)
    


if __name__=="__main__":
    solution()
