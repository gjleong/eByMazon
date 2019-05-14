# In this file I write the code needed for our main python file to manipulate mongodb
# I have code for actions such as......
#    - create a super user
#    - create an oridinary user (pending for super user)
#    - create items (pending for super user)
#    - move pending items to accepted or rejected list
#


from pymongo import MongoClient
from pymongo import ReturnDocument
import json

def connect_db():
    client = MongoClient("localhost", 27017)
    return client

client = connect_db()
db = client['wnbDatabase']

#----------------------- Super User so you can continue your code -------------------
SU = db.SU()
su1 = {         #created at runtime
    "username": "superuser1",
    "password": "winenbuy"
}
result = SU.insert_one(su1)
print(result) #may be deleted, it just print if it was successful

#----------------------- Several OUs created so you can continue your code-------------
#created when signing up
#list of GU applications in which the SU can accept or deny
OUPending = db.OUPending
new_ou = {
    "fname": "Leah",
    "lname": "Meza",
    "email": "me@gmail.com",
    "creditnum": "466443342"
}
result = OUPending.insert_one(new_ou)
print(result) #may delete

new_ou = {
    "fname": "Fatima",
    "lname": "Reeza",
    "email": "fr@gmail.com",
    "creditnum": "88483445"
}
result = OUPending.insert_one(new_ou)
print(result) #may delete

new_ou = {
    "fname": "Krystal",
    "lname": "Leong",
    "email": "kl@gmail.com",
    "creditnum": "3645447498"
}
result = OUPending.insert_one(new_ou)
print(result) #may delete

new_ou = {
    "fname": "Marianna",
    "lname": "Fervenza",
    "email": "mf@gmail.com",
    "creditnum": "6483721873"
}
result = OUPending.insert_one(new_ou)
print(result) #may delete

#---------------------------------- PUT ANY PRE LISTED ITEMS HERE ----------------------
#follow template
ItemPending = db.ItemPending
new_item = {
    "id_": 1,      #INCREMENT LIKE A DATABASE
    "title": "Nice Blue Shirt",
    "keywords": "blue;shirt;short sleeve", #separated by ;
    "price": "buy:$35",
    "image": "img/1.png" #image folder/id_.png
}
result = ItemPending.insert_one(new_item)
print(result) #may delete

new_item = {
    "id_": 2,      #INCREMENT LIKE A DATABASE
    "title": "",
    "keywords": "", #separated by ;
    "price": "",
    "image": "img/2.png" #image folder/id_.png
}
result = ItemPending.insert_one(new_item)
print(result) #may delete

#to move to Item (Item accepted) or ItemRejected is similar to OU
Items = db.Items
ItemRejected = db.ItemRejected

#------------------------------- SUGGESTED ACTIONS TO MONGODB --------------------------
#---------- USE AS REFERENCE FOR YOUR PAGES , DELETE LATER -----------------------------

#once they log in, we need to store all their information and save as CONST values
#so they can be queried by pymongo and manipulated
EMAIL_OU = "me@gmail.com" #obtained after sign in
myquery = { "address": EMAIL_OU }
result = EMAIL_OU.delete_one(myquery)
#---- i will use above to perform below dynamically

#created when SU accepts application
#list of approved OU (each will have their own profile)
ou_accepted = new_ou
OU = db.OU #accepted ordinary users, ALL TABLE SHOULD BE CREATED AT THE TOP LATER
result = OUPending.delete_one({ "email" : "me@gmail.com"})
print(result)
result = OU.insert_one(ou_accepted)
print(result)

#creted when SU rejects application
#list of rejected OU used for SU records
ou_rejected = new_ou
OU = db.OU #accepted ordinary users, ALL TABLE SHOULD BE CREATED AT THE TOP LATER
result = OUPending.delete_one({ "email" : "me@gmail.com"})
print(result)
result = OU.insert_one(ou_accepted)
print(result)

#----- if a whole list is moved .bulk_write() does multiple actions in one call
cursor_excess_new = (
    db.test_collection_new.find().sort([("_id", 1)]).limit()
)
queries = [InsertOne(doc) for doc in cursor_excess_new]
db.test_collection_old.bulk_write(queries)


#-------------------------------------------------
# how i plan to read a json file after html form
OUPending = db.OUPending
page = open("OUPending.json", 'r')
user = json.loads(page.read())
OUPending.insert_one(user)

#---------------------- ACCESS A COLLECTION FOR RAW DATA-----------------







#---- template for a class we might use
class PymongoManagement:
    def __intit__(self):
        self.client = MongoClient("localhost", 27017)
        return client
    
    def insert_one_gu(collection, gu):
        collection.insert_one(gu)
    
    def gu_accepted(collection, gu):
        collection.delete_one({ "email" : EMAIL})
        collection.insert_one(gu)

    def gu_rejected(collection, gu):
        collection.delete_one({ "email" : EMAIL})
        collection.insert_one(gu)

if __name__ == "__main__":
    mongoDB = PymongoManagement()
    mongoDB = connect_db()
    db = mongoDB['wnbDatabase']
