import pymongo

myclient = pymongo.MongoClient("mongodb+srv://students:321321@firstcluster-bxilw.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["students"]


#sort("name", 1) #ascending
#sort("name", -1) #descending
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)