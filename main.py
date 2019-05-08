# -*- coding: utf-8 -*-
"""
eByMazon
Choux Cream (Assigned Team #2)
"""
# Handle web requests
import jinja2
import os
import webapp3
#from paste import httpserver
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import requests

# for data storage and encryption: make it non-human readable since
# we are storing user information 
import pickle
# for unique user id with id = uuid.uuid4()
# uuid4 is more secure than uuid1
# UUID('XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX') where X's are hex values
import uuid
# parse urls
#import urllib.parse
#import logging


jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

# user databases will be stored as either files or dictionaries
# pickle and load
LISTINGS = {}    
APPLICATIONS = {}
LOGIN = {}
ORDINARY_USERS = {}
SUPER_USERS = {}

def GetMostPopularItems():
    return 'popular items'
def GetMostPopularOUs():
    return 'popular OUs'

'''
###############################################################################
PRODUCTS AND LISTINGS
###############################################################################
'''
class Product:

    def __init__(self, product_id, product_name, product_categories):
        self.product_id = product_id
        self.product_name = product_name
        self.product_categories = product_categories

    def GetProductID(self):
        return self.product_id
    def GetProductName(self):
        return self.product_name
    def GetProductCategories(self):
        return self.product_categories

class Listing:
    def __init__(self, listing_id, seller_id, product_id, price, buy_now, bid):
        self.listing_id = listing_id
        self.seller_id = seller_id
        self.product_id = product_id
        self.price = price
        self.buy_now = buy_now
        self.bid = bid
    def GetListingID(self):
        return self.listing_id
    def GetSellerID(self):
        return self.seller_id
    def GetProductID(self):
        return self.product_id
    def GetPrice(self):
        return self.price
    def CanBuyNow(self):
        return self.buy_now
    def CanBid(self):
        return self.bid

'''
###############################################################################
USERS
###############################################################################
'''
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def GetName(self):
        return self.name
    def GetEmail(self):
        return self.email
    def SetName(self, name):
        self.name = name
    def SetEmail(self, email):
        self.email = email

class OrdinaryUser(User):
    def __init__(self):
        super().__init__(self)
    # Get
    def GetOUID(self):
        return self.ou_id
    def GetName(self):
        return super().GetName(self)
    def GetEmail(self):
        return super().GetEmail(self)
    def GetAddress(self):
        return self.address
    def GetPhoneNumber(self):
        return self.phone_number
    def GetCreditCard(self):
        return self.credit_card
    # Set
    # OU is not allowed to change their user id
    def SetName(self, name):
        self.name = super().SetName(self, name)
    def SetEmail(self, email):
        self.email = super().SetEmail(self, email)
    def SetAddress(self, address):
        self.address = address
    def SetPhoneNumber(self, phone_number):
        self.phone_number = phone_number
    def SetCreditCard(self, credit_card):
        self.credit_card = credit_card
    
'''
SuperUser has a higher level of access, compared to OrdinaryUser
'''
class SuperUser(User):
    def __init__(self):
        super().__init__(self)
    def GetSUID(self):
        return self.GetID(self)
    def GetName(self):
        return super().GetName(self)
    def GetEmail(self):
        return super().GetEmail(self)
    
class RegistrationApplicant:
    def __init__(self, application_id, name, email, phone_number, address, payment):
        self.application_id = application_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.payment = payment

'''
###############################################################################
PAGE HANDLERS
###############################################################################
'''


class MainHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render())
        
    
    
class RegisterHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/register.html')
        self.response.write(template.render())
    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        phone_number = self.request.get('phone_number')
        address = self.request.get('address')
        credit_card = self.request.get('credit_card')
        data = {'name': name, 'email': email, 'phone_number': phone_number,
                'address': address, 'credit_card': credit_card, 'signup': 'submit'}
        
        # generate random key
        # check that key does not already exist in db
        key = uuid.uuid4()
        ou_applicant = RegistrationApplicant(key, name, email, phone_number, address, credit_card)
        
        # if approved then we will make an OU from this information
        # for human readable testing purposes
#        ou_applicant = {
#                'name': name,
#                'email': email,
#                'phone_number': phone_number,
#                'address': address,
#                'credit_card': credit_card
#        }
        
        APPLICATIONS.update({key: ou_applicant})
        
#        ou_applicant_key = ou_applicant.put()
        requests.post('https://gjleong.github.io/eByMazon', data=data)
        self.redirect('/confirmation')

class ConfirmationHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/confirmation.html')
        self.response.write(template.render())
    

app = webapp3.WSGIApplication([
        ('/', MainHandler),
        ############################# GET ONLY
#        ('/about', AboutHandler),
#        ('/privacy', PrivacyHandler),
#        ('/terms', TermsHandler),
#        ('/return', ReturnHandler),
#        ('/careers', CareersHandler),
#        ('/contact', ContactHandler),
        ############################## GET & POST
#        ('/user/([0-9]+))', Redirect),
#        ('/user/([0-9]+))/cart', CartHandler),
#        ('/login', LoginHandler)
        ('/register', RegisterHandler),
        ('/confirmation', ConfirmationHandler),
#        ('/user/([0-9]+))/settings', SettingsHandler),
#        ('/superuser', SuperUserHandler),
#        ('/error', ErrorPageHandler),
        ], debug=True)
#domain = "gjleong.github.io"
#app.config['SERVER_NAME'] = domain

def main():
    # initialize users when starting up the server
    try:
        with open("listings.txt", "rb") as handle:
            global LISTINGS
            LISTINGS = pickle.loads(handle.read())
    except EOFError as e:
        pass
    try:
        with open("applications.txt", "rb") as handle:
            global APPLICATIONS
            APPLICATIONS = pickle.loads(handle.read())
    except EOFError as e:
        pass
    try:
        with open("login.txt", "rb") as handle:
            global LOGIN
            LOGIN = pickle.loads(handle.read())
    except EOFError as e:
        pass
    try:
        with open("ordinary_users.txt", "rb") as handle:
            global ORDINARY_USERS
            ORDINARY_USERS = pickle.loads(handle.read())
    except EOFError as e:
        pass
    try:
        with open("super_users.txt", "rb") as handle:
            global SUPER_USERS
            SUPER_USERS = pickle.loads(handle.read())
    except EOFError as e:
        pass
#    global app
#    app.run()
    httpd = make_server('127.0.0.1', 8080, app)
    httpd.serve_forever()
    
# we don't necessarily want to shut down the application
def shut_down(*args, **kwargs):
    global app
#    app.shutdown()
#    app.stop()
    with open("listings.txt", "wb") as handle:
        global LISTINGS
        pickle.dump(LISTINGS, handle)
    with open("applications.txt", "wb") as handle:
        global APPLICATIONS
        pickle.dump(APPLICATIONS, handle)
    with open("login.txt", "wb") as handle:
        global LOGIN
        pickle.dump(LOGIN, handle)
    with open("ordinary_users.txt", "wb") as handle:
        global ORDINARY_USERS
        pickle.dump(ORDINARY_USERS, handle)
    with open("super_users.txt", "wb") as handle:
        global SUPER_USERS
        pickle.dump(SUPER_USERS, handle)

if __name__ == '__main__':
#    app.start()
    main()
    shut_down()
    print(APPLICATIONS)