from google.appengine.ext import ndb
from google.appengine.api import search
from datetime import datetime

class UserData():
    user_name = ndb.TextProperty()
    Date = ndb.DateTimeProperty(auto_now_add=True)
    user_email = ndb.TextProperty()
    user_image = ndb.BlobProperty()

class ImageData():
    user_name = ndb.StringProperty()
    image = ndb.BlobProperty()
    

    

