from google.appengine.ext import ndb
from google.appengine.api import search
from datetime import datetime

class UserData(ndb.Model):
    user_name = ndb.StringProperty()
    Date = ndb.DateTimeProperty(auto_now_add=True)
    user_email = ndb.TextProperty()
    user_image = ndb.BlobProperty()
    
    
class Updates(ndb.Model):
    notifications = ndb.StringProperty()


    

    

