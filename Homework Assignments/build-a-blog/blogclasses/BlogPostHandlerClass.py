import webapp2
import setup_jinja

from blogclasses import BlogPostClass

jinja_env = setup_jinja.setup_jinja()


class BlogPostHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/blog-post' 
    """

    def get(self, blogpostid=None):
        """ Displays a list of all blog posts if no blog post id is submitted
            If a blog post id is submitted only shows the blog post for the specified ID
        """

        print(blogpostid)
        pass

