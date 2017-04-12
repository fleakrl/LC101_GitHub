from google.appengine.ext import db


class BlogPost(db.Model):
    """class that defines a blog post"""
    title = db.StringProperty(required=True)
    content = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

