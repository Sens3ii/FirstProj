import pymongo

myclient = pymongo.MongoClient("mongodb+srv://students:321321@firstcluster-bxilw.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

for x in mycol.find():
    print(x)
