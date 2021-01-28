import pymongo

myclient = pymongo.MongoClient("mongodb+srv://students:321321@firstcluster-bxilw.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]

mycol = mydb["students"]
print(mydb.list_collection_names()) #Return a list of all collections in your database

collist = mydb.list_collection_names()
if "students" in collist: #Check if the "students" collection exists
  print("The collection exists.")