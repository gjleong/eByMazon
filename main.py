# -*- coding: utf-8 -*-
"""
eByMazon
Choux Cream (Assigned Team #2)
Marianna Fervenza, Krystal Leong, Leah Meza, Fathima Mohammed Reeza
"""
# Handle web requests
import jinja2
import os
import webapp2
# for unique user id with id = uuid.uuid4()
import uuid
# 
import logging

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
Item objects to sell
'''
class Item:
    listing_id
    product_id
    price
    sell_method
    def __init__(self, listing_id, product_id, price, sell_method):
        self.listing_id = listing_id
        self.product_id = product_id
        self.price = price
        self.sell_method = sell_method
    def GetPrice(self):
        return price
    def GetProductID(self):
        return product_id
    def GetListingID(self):
        return listing_id
    def GetSellMethod(self):
        return sell_method

'''
Guest user objects
Guest users are NOT registered.
Object sends information when submitting application
'''
# guest users are NOT registered; it saves nothing about the user until submitting appl
class GuestUser:
    def Browse(title, keywords, price_nature, picture):
        print('browsing')
    def AddToCart():
        Login()
    def SubmitApplication(self, name, address, phone_number, ccnum):
        # generate appl id
        # send user info tuple with appl id
        APPLICATIONS.append({})
        print('submit appl')
        
class OrdinaryUser(GuestUser):
    user_id
    user_ratings = {}  # user_id: rating
    vip_status = false
    cart = {}
    search_history = []  # based on keywords used
    num_purchases = 0
    def __init__(self, name, phone_number, ccnum):
        self.name = name
        self.phone_number = phone_number
        self.ccnum = ccnum
    def AddToCart(self, item):
        
    def GetUserRatings(self):
        return self.user_ratings
    # should also/have separate fn to update when new rating submitted
    def GetOverallRating(self):
        for rating in self.user_ratings:
            
    def GetRecommendations():
        if search_history == None and num_purchases == 0:
            GetMostPopularItems()
            GetMostPopularOUs()
    def CheckOut(self, purchase_price):
        # change to template render
        print('Card has been charged', purchase_price)
    def GetCart(self):
        return cart
    def Purchase(self, listing_id):
        cart = GetCart(self)
        purchase_price = 0.00
        for item in cart:
            purchase_price = purchase_price + item.GetPrice()
        if vip_status:
            purchase_price = purchase_price * 0.95
        CheckOut(self, purchase_price)
        
    def Sell(self):
        
    def RequestListing(self, title, keywords, price_nature, picture):
        # generate listing_id
        # generate notifications on keywords
    def RequestItem(self, keywords):
        
    def Notify():
        
    def UpgradeVIP(self):
        self.vip_status = true
    def DowngradeOU(self):
        self.vip_status = false

class SuperUser:
    def __init__(self):
        print('SU')
    def WarnOU(message):
        #submit message via user_id
    def TabooCensor(listing_id):
        
    def ApproveApplication(application_id):
        APPLICATIONS[application_id]
    def RejectApplication(application_id):
        
    def ApproveListing(listing_id):
        TabooCensor()
    def RejectListing(listing_id):
        WarnOU("Rejection reason")
        
#########################             HANDLERS    #############################   
# home page should redirect to login, product, or search pages (or category overlay)
class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/home.html')
        self.response.write(template.render())






# handle information on user account page
class UserHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/home.html')
        self.response.write(template.render())
    def post(self):
        email = self.request.get('email')
        password = self.request.get('password')
        if LOGIN[email] == password:
            if email == password:
            # trigger pw reset
        elif LOGIN[email] != password:
            
        
        
        
        
        
        
        
        
class SuperUserHandler(webapp2.RequestHandler):
    
    # approve a user request to register
    # req name, addr, phone, cc
    def post(self, unique_id):
#        template_val = 'templates/superuser.html'

        email = APPLICATIONS[unique_id][0]
        name = APPLICATIONS[unique_id][1]
        phone_number = APPLICATIONS[unique_id][2]
        address = APPLICATIONS[unique_id][3]
        ccnum = APPLICATIONS[unique_id][4]
        
        # set password to email initially
        LOGIN[email] = tuple(unique_id, email)
        ORDINARY_USERS[unique_id] = OrdinaryUser(name, address, phone_number, ccnum)
#        url_val = '/user/OU_' + unique_id
#        template = jinja_environment.get_template(template_val)
#        self.response.write(template.render())
        self.redirect('templates/superuser')
    
    
    
class CartHandler(webapp2.RequestHandler):
    # get all items in cart
    def get(self):
        template = jinja_environment.get_template('templates/cart.html')
        self.response.write(template.render())
    # checkout
    def post(self):
        # send list of items in cart
    
    
class CheckoutHandler(webapp2.RequestHandler)
    def get(self):
        
    
    
    
    
class UserSettingsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/user/' +  + 'settings.html')
        self.response.write(template.render())
        
        
        
        
        
        
        
        
        
###############################################################################
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/login.html')
        self.response.write(template.render())
    def post(self):
        email = self.request.get('email')
        password = self.request.get('password')
        if password == LOGIN[email][1]:
            template_val = 'templates/login.html'
            url_val = '/login'
            template = jinja_environment.get_template(template_val)
            self.response.write(template.render({'email': email, 'password': password}))
            self.redirect(url_val)
        message = 'Invalid Login.'
        template = jinja_environment.get_template('templates/login.html')
        self.response.write(template.render({'message': message}))
###############################################################################
class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/register.html')
        self.response.write(template.render())
    def post(self):
        unique_id = uuid.uuid4().int
        name = self.request.get('name')
        email = self.request.get('email')
#        password = self.request.get('password')
        address = self.request.get('address')
        phone_number = self.request.get('phone_number')
        ccnum = self.request.get('ccnum')
        # submit request to join ONLY
        APPLICATIONS[unique_id] = tuple(email, name, phone_number, address, ccnum)
        
        
        

###############################################################################
class ListingHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/product.html')
        self.response.write(template.render())
        
        
        
        
        
        
class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/settings.html')
        self.response.write(template.render())        
        

class MessageHandler(webapp2.RequestHandler):
    def get(self):
        
        
        
        
# links at bottom of page
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/about.html')
        self.response.write(template.render()) 
class PrivacyHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/privacy.html')
        self.response.write(template.render()) 
class TermsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/tos.html')
        self.response.write(template.render())
class ReturnHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/return.html')
        self.response.write(template.render()) 
class CareersHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/careers.html')
        self.response.write(template.render()) 
class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/contact.html')
        self.response.write(template.render())
    def post(self):
        # to contact require min email and message
        email = template.request.get('email')
        message = template.request.get('message')
        # do something with this
        

app = webapp2.WSGIApplication([
        ('/', MainHandler),
        #############################
        ('/about', AboutHandler),
        ('/privacy', PrivacyHandler),
        ('/terms', TermsHandler),
        ('/return', ReturnHandler),
        ('/careers', CareersHandler),
        ('/contact', ContactHandler),
        ##############################
        ('/user/([0-9]+))', Redirect),
        ('/user/([0-9]+))/cart', CartHandler),
        ('/login', LoginHandler)
        ('/register', RegisterHandler),
        ('/user/([0-9]+))/settings', SettingsHandler),
        ('/superuser', SuperUserHandler)
        ], debug = True)
