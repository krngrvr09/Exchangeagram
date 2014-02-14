from google.appengine.ext import ndb
from google.appengine.api import search
from datetime import datetime

class UserData(ndb.Model):
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    contributed_to = ndb.StringProperty()
    paid = ndb.IntegerProperty()
    started = ndb.StringProperty()
    picture = ndb.BlobProperty()
    description = ndb.TextProperty()
    title = ndb.StringProperty()
    payment = ndb.IntegerProperty()


# Create a document.
doc = search.Document(
    doc_id='document-id',
    fields=[search.TextField(name='subject', value='my first email'),
            search.HtmlField(name='body', value='<html>some content here</html>')])

# Index the document.
try:
    index.put(doc)
except search.PutError, e:
    result = e.results[0]
    if result.code == search.OperationResult.TRANSIENT_ERROR:
        # possibly retry indexing result.object_id
except search.Error, e:
    # possibly log the failure


# Query the index.
try:
    results = index.search('subject:first body:here')

    # Iterate through the search results.
    for scored_document in results:
        # process the scored_document

except search.Error, e:
    # possibly log the failure

query = "stories"
try:
  index = search.Index(INDEX_NAME)
  search_results = index.search(query)
  for doc in search_results:
    # process doc ..
except search.Error:
  # ...

