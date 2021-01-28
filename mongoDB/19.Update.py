import pymongo

myclient = pymongo.MongoClient("mongodb+srv://students:321321@firstcluster-bxilw.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

myquery = { "name": "Daniil" }
newvalues = { "$set": { "name": "Alesha" } }

mycol.update_one(myquery, newvalues)

#print "students" after the update:
for x in mycol.find():
  print(x)