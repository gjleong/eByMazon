# -*- coding: utf-8 -*-
"""
eByMazon
Choux Cream (Assigned Team #2)
"""
# Handle web requests
import jinja2
import os
import webapp3
# for unique user id with id = uuid.uuid4()
#import uuid
# parse urls
#import urllib.parse
#import logging

# will we need these?
#import requests
#from BeautifulSoup import BeautifulSoup

jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

# user databases will be stored as either files or dictionaries

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
Product objects to sell
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
        return product_id
    def GetPrice(self):
        return self.price
    def CanBuyNow(self):
        return self.buy_now
    def CanBid(self):
        return self.bid

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
HANDLERS
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
    def register(self):
        name = self.request.get('name')
        email = self.request.get('email')
        phone_number = self.request.get('phone_number')
        address = self.request.get('address')
        credit_card = self.request.get('credit_card')
        
        # generate random key
        key = "63165165213265"
        ou_applicant = RegistrationApplicant(key, name, email, phone_number, address, credit_card)
        
        # if approved then we will make an OU from this information
#        ou_applicant = {
#                'name': name,
#                'email': email,
#                'phone_number': phone_number,
#                'address': address,
#                'credit_card': credit_card
#        }
        
        APPLICATIONS.update({key: ou_applicant})
        
#        ou_applicant_key = ou_applicant.put()
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render())

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
#        ('/superuser', SuperUserHandler)
        ], debug = True)
#app.config['SERVER_NAME'] = 'https://gjleong.github.io/eByMazon'

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port=8080)

if __name__ == '__main__':
    main()
    print(APPLICATIONS)