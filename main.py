# -*- coding: utf-8 -*-
"""
eByMazon
Choux Cream (Assigned Team #2)
"""
# our modules
import su
import ou
import gu
import items
# import wndDatabase

import json

# Handle web requests
import jinja2
import os
import webapp3
from paste import httpserver
import requests
# generate secure tokens for users
import secrets
# database and authentication
from pymongo import MongoClient
# parse urls
#import urllib.parse
#import logging

def connect_db():
    client = MongoClient("localhost", 27017)
    return client

client = connect_db()
db = client['wnbDatabase']

jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))


'''
###############################################################################
COLLECTIONS/TABLES
###############################################################################
'''
if not "USERS" in db.list_collection_names():
    USERS = db["USERS"] # user info, cart, friends
if not "USERS_PENDING" in db.list_collection_names():
    USERS_PENDING = db["USERS_PENDING"]
if not "AUTH" in db.list_collection_names():
    AUTH = db["AUTH"]
if not "SU_AUTH" in db.list_collection_names():
    SU_AUTH = db["SU_AUTH"]
if not "ITEMS" in db.list_collection_names():
    ITEMS = db["ITEMS"]
if not "ITEMS_PENDING" in db.list_collection_names():
    ITEMS_PENDING = db["ITEMS_PENDING"]
if not "ITEMS_REQUESTED" in db.list_collection_names():
    ITEMS_REQUESTED = db["ITEMS_REQUESTED"]


def Average_Rating(user, new_rating):
    sum_rating = sum_rating + new_rating
    num_ratings = num_ratings + 1
    return float(sum_rating/num_ratings)

def GetMostPopularItems():
    return 'popular items'
def GetMostPopularOUs():
    return 'popular OUs'

'''
###############################################################################
GUEST/ORDINARY USER HANDLERS
###############################################################################
'''
# View account information
class AccountHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/account.html')
        self.response.write(template.render())
    
# Edit account information
class AccountEditHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/account_edit.html')
        self.response.write(template.render())
        
    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        phone_number = self.request.get('phone_number')
        address = self.request.get('address')
        credit_card = self.request.get('credit_card')
        
        # get ou_id of current user
        db.getUser()
        # TODO: update with new parameters in database
        
        
        self.redirect('/account')

# Add item to cart
class AddToCartHandler(webapp3.RequestHandler):
    def post(self):
        # get current item details from db
        # update total purchase cost
        # update cart
        print()
        
# Purchase items in cart     
class CheckoutHandler(webapp3.RequestHandler):   
    def processpayment(self):
        # get current user info
        # charge credit card
        # continue shopping/back to home
        self.redirect('/')
      
# Confirmation for registration request
class ConfirmationHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/confirmation.html')
        self.response.write(template.render())

# Handler for submitting a listing to be approved by an SU.
class ItemListingRequestHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/item#listing.html')
        self.response.write(template.render())        
    def post(self):
        title = self.request.get('title')
        keywords = self.request.get('keywords')
        # set price option on radio button selection
        price_option
        image = self.request.get('image')
        # title
        # TODO: edit btn_name to name of button on form
        data = {'title': title, 'keywords': keywords, 'price_option': price_option, 'image': image, 'btn_name': 'submit'}
        
        item_pending = {'title': title, 'keywords': keywords, 'price_option': price_option, 'image': image}
        ITEMS_PENDING.insert_one(item_pending)
        
        requests.post('https://gjleong.github.io/eByMazon', data=data)
        self.redirect('/confirmation')
        
        # add record to item request db
# Item Listing page
class ItemDetailHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/item#detail.html')
        self.response.write(template.render())
        
# Login
class LoginHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/login.html')
        self.response.write(template.render())
    def post(self):
        email = self.request.get('email')
        password = self.request.get('password')
        
        # TODO: validate against db (auth)
        if AUTH[email].password == password:
            session.logged_in = True

# Logout 
class LogoutHandler(webapp3.RequestHandler):
    def post(self):
        session.logged_in = False
    
# Add rating to item
class RateItemHandler(webapp3.RequestHandler):
    def post(self):
        # Assert that user has purchased item
        item_to_rate = self.request.get('item_to_rate')
        new_rating = self.request.get('rating')
        avg_rating = AverageRating(item_to_rate, new_rating)
        # update avg_rating

# Add rating to seller
class RateSellerHandler(webapp3.RequestHandler):
    def post(self):
        # Assert that user has purchased from seller
        user_to_rate = self.request.get('user_to_rate')
        new_rating = self.request.get('rating')
        avg_rating = AverageRating(user_to_rate, new_rating)
        # update avg_rating

# Registration page
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
        # TODO: ensure that user is not in db, then add
        data = {'name': name, 'email': email, 'phone_number': phone_number,
                'address': address, 'credit_card': credit_card, 'signup': 'submit'}
        
        key = secrets.token_hex()
        # TODO: check that key does not already exist in db
                
        # if approved then we will make an OU from this information
        ou_applicant = {
                'name': name,
                'email': email,
                'phone_number': phone_number,
                'address': address,
                'credit_card': credit_card
        }
        
        USERS_PENDING.insert_one(ou_applicant)
#        APPLICATIONS.update({key: ou_applicant})
        
#        ou_applicant_key = ou_applicant.put()
        requests.post('https://gjleong.github.io/eByMazon', data=data)
        self.redirect('/confirmation')

# Handler for requesting an item not found in the system.
class RequestItemHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/item#request.html')
        self.response.write(template.render())
    def post(self):
        keywords = []
        # title
        # TODO: edit btn_name to name of button on form
        data = {'keywords': keywords, 'btn_name': 'submit'}
        
        item_request = {'keywords': keywords}
        ITEMS_REQUESTED.insert_one(item_request)
        
        requests.post('https://gjleong.github.io/eByMazon', data=data)
        self.redirect('/confirmation')
# Search/browse items filtered from database
class SearchHandler(webapp3.RequestHandler):
    def post(self):
        search_query = self.request.get('search')
        
# Other settings
class SettingsHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/settings.html')
        self.response.write(template.render())
        
# View items in cart
class ViewCartHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/cart.html')
        self.response.write(template.render())
    def checkout(self):
        self.redirect('/checkout')

# View summary about seller
class ViewSellerInfoHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/seller.html')
        # pull info from table based on seller id/email/name
        self.response.write(template.render())

# View history of transactions
class ViewTransactionsHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/transaction#history.html')
        self.response.write(template.render())

'''
###############################################################################
EXTRA FEATURE
###############################################################################
'''
# Feature for users to check if their account has been approved directly from
# the login page.
class CheckAccountStatusHandler(webapp3.RequestHandler):
    def post(self):
        email = self.request.get('email')
        # check for email in accepted applications
        self.response.write()

'''
###############################################################################
SUPER USER HANDLERS
###############################################################################
'''
class SULoginHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/su#login.html')
        self.response.write(template.render())
    def post(self):
        # TODO: authenticate against db
        print()
        
class SUManageHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/su#manage.html')
        self.response.write(template.render())

class GUAppSummaryHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/guapp#summary.html')
        self.response.write(template.render())
    
class GUAppDetailHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/guapp#detail.html')
        self.response.write(template.render())
    def post(self):
        # TODO: post request for accept/reject
        print()
    
class ItemListingRequestHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/itemapp#detail.html')
        self.response.write(template.render())
    

'''
###############################################################################
OTHER HANDLERS <GET-ONLY>
###############################################################################
'''
class AboutHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/about.html')
        self.response.write(template.render())
class PrivacyHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/privacy.html')
        self.response.write(template.render())
class TermsHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/terms.html')
        self.response.write(template.render())
class ReturnHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/return.html')
        self.response.write(template.render())
class CareersHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/careers.html')
        self.response.write(template.render())
class ContactHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/contact.html')
        self.response.write(template.render())

class ErrorHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/error.html')
        self.response.write(template.render())
'''
###############################################################################
APP
###############################################################################
'''
class MainHandler(webapp3.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render())

app = webapp3.WSGIApplication([
        ('/', MainHandler), #index.html
        ############################# GET ONLY
        ('/about', AboutHandler),
        ('/privacy', PrivacyHandler),
        ('/terms', TermsHandler),
        ('/return', ReturnHandler),
        ('/careers', CareersHandler),
        ('/contact', ContactHandler),
        ############################## GET & POST
        ('/account', AccountHandler),
        ('/account#edit', AccountEditHandler),
         ('item#detail', ItemDetailHandler),
        ('/itemlisting#request', ItemListingRequestHandler),
        ('/cart', ViewCartHandler),
        ('guapp#summary', GUAppSummaryHandler),
        ('guapp#detail', GUAppDetailHandler),
#        ('/homeGU', HomeGUHandler),
        ('/login', LoginHandler),
        ('/register', RegisterHandler),
        ('/confirmation', ConfirmationHandler),
        ('/settings', SettingsHandler),
        ('/superuser', SULoginHandler),  # SU Main.html
        ('/error', ErrorHandler),
        ], debug=True)
#domain = "gjleong.github.io"
#app.config['SERVER_NAME'] = domain

def main():
    httpserver.serve(app, host='127.0.0.1', port=10061)
    
# we don't necessarily want to shut down the application
def fin():
    global app
    app.shutdown()

if __name__ == '__main__':
    main()