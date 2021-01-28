import pymongo

myclient = pymongo.MongoClient("mongodb+srv://students:321321@firstcluster-bxilw.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

mydict = {"name": "Daniil", "surname": "Koilybayev", "id": "19B030600"}

x = mycol.insert_one(mydict) #Insert a record in the "students" collection

print(x.inserted_id) #return the value of the _id field
