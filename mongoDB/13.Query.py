import pymongo

myclient = pymongo.MongoClient("mongodb+srv://students:321321@firstcluster-bxilw.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

myquery = { "address": { "$regex": "^S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)