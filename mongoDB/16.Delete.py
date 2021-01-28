import pymongo

myclient = pymongo.MongoClient("mongodb+srv://students:321321@firstcluster-bxilw.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

myquery = { "address": {"$regex": "^H"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, "documents deleted")