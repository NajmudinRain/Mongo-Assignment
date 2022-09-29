from ast import GtE
from operator import gt
from pymongo import MongoClient
import pandas as pd
from pprint import pprint
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
    # Insert the given data ( data is present inside data.json file ), to "details" collection, inside your "Employees" database. Make sure you are using python to insert the data. Do commit this python file in your repository.
    data=data.to_dict(orient="records")
    db=localConn['Employees']
    if 'details' not in db.list_collection_names():
        db.details.insert_many(data)
    # After inserting all the documents -> display all the documents. 2.1 Using find() 2.2 Using aggregate()
    res=db.details.find({})
    # reslist=list(res)
    # for i in reslist:
    #     print(i)

    # res=db.details.aggregate([])
    # reslist=list(res)
    # for i in reslist:
    #     pprint(i)
# Display the fields --> name, salary, marital status and company of all the documents. ( Make sure no 
#    other fields should be displayed apart from the above mentioned fields. )

    # res=db.details.find({},{"name":1,"Marital Status":1, "company":1,"_id":0})
    # reslist=list(res)
    # for i in reslist:
    #     pprint(i)
# Display **only** the **name** field of all the documents which are from Norway.
    # res=db.details.find({"country":"Norway"},{"name":1,"_id":0})
    # reslist=list(res)
    # for i in reslist:
    #     pprint(i)

    # Display all the documents in descending order which have salary greater than equal to 3500

    # res=db.details.find({"salary":{"$gte":3500}}).sort("salary",-1)
    # print(res)
    # reslist=list(res)
    # for i in reslist:
    #     pprint(i)
# Find all the documents which are from New Zealand and are married
    # res=db.details.find({"country":"New Zealand","Marital Status":"Married"})
    # print(res)
    # reslist=list(res)
    # for i in reslist:
    #     pprint(i)

#   Display the names and salary of top 10 documents with least amount of salary.
    res=db.details.find({},{"name":1,"salary":1,"_id":0}).sort("salary",1).limit(10)
    print(res)
    reslist=list(res)
    for i in reslist:
        pprint(i)




if __name__=="__main__":
    solution()
