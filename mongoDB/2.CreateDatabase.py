import pymongo

myclient = pymongo.MongoClient("mongodb+srv://students:321321@firstcluster-bxilw.gcp.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["mydatabase"]

print(myclient.list_database_names()) #Return a list of your system's databases

dblist = myclient.list_database_names()
if "mydatabase" in dblist: #Check if "mydatabase" exists
  print("The database exists.")
