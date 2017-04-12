import webapp2
import setup_jinja
from google.appengine.ext import db

jinja_env = setup_jinja.setup_jinja()


class MainHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/' 
    """
    def get(self):
        blogposts = db.GqlQuery("SELECT * FROM BlogPost")
        t = jinja_env.get_template("frontpage.html")
        content = t.render(blogposts = blogposts)
        self.response.write(content)


