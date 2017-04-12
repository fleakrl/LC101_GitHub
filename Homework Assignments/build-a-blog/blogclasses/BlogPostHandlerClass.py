import webapp2
import setup_jinja
from google.appengine.ext import db

jinja_env = setup_jinja.setup_jinja()


class BlogPostHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/blog-post' 
    """

    def get(self, blogpostid=None):
        """ Displays a list of all blog posts if no blog post id is submitted
            If a blog post id is submitted only shows the blog post for the specified ID
        """
        if blogpostid == None:
            blogposts = db.GqlQuery("SELECT * FROM BlogPost ORDER BY created DESC")
            t = jinja_env.get_template("master_list_table.html")
            content = t.render(blogposts=blogposts)
            self.response.write(content)
        else:
            blogpostid = int(blogpostid)
            blogposts = db.GqlQuery("SELECT * FROM BlogPost WHERE id IS blogpostid")
            t = jinja_env.get_template("master_list_table.html")
            content = t.render(blogposts=blogposts)
            self.response.write(content)

