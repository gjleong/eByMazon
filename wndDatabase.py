from pymongo import MongoClient
from pymongo import InsertOne
import json

def connect_db():
    client = MongoClient("localhost", 27017)
    return client

client = connect_db()
db = client['wnbDatabase']

#created when signing up
#list of OU in which the SU can accept or deny
OUPending = db.OUPending
new_ou = {
    "fname": "Leah",
    "lname": "Meza",
    "email": "me@gmail.com",
    "creditnum": "466443342"
}
result = OUPending.insert_one(new_ou)
print(result)

#created when SU accepts application
#list of approved OU (each will have their own profile)
ou_accepted = new_ou
OU = db.OU
result = OU.delete_one({new_ou : 1})
print(result)
result = OU.insert_one(ou_accepted)
print(result)

#creted when SU rejects application
#list of rejected OU used for SU records
cursor_excess_new = (
    db.test_collection_new
      .find()
      .sort([("_id", 1)])
      .limit()
)

queries = [InsertOne(doc) for doc in cursor_excess_new]
db.test_collection_old.bulk_write(queries)


#-------------------------------------------------
# how i plan to read a json file after html form
OUPending = db.OUPending
page = open("OUPending.json", 'r')
user = json.loads(page.read())
OUPending.insert_one(user)



