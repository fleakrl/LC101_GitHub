import webapp2
import setup_jinja
import cgi

from blogclasses import BlogPostClass

jinja_env = setup_jinja.setup_jinja()


class NewPostHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/new-post' 
    """
    def get(self):
        t = jinja_env.get_template("new_blog_post.html")
        content = t.render()
        self.response.write(content)

    def post(self):
        new_post_title = self.request.get("post_title")
        new_post_content = self.request.get("post_content_text")

        # if the user typed nothing at all, redirect and yell at them
        if (not new_post_title) or (not new_post_content) or \
                (new_post_title.strip() == "") or (new_post_content.strip() == ""):
            error = "All fields are required."
            self.redirect("/new-post?error=" + cgi.escape(error))

        """ Adds a new blog post to the database & redirects to main page """
        blog_post = BlogPostClass.BlogPost(title = new_post_title, content = new_post_content)
        blog_post.put()

        self.redirect('/')
