import webapp2
import setup_jinja
import cgi

from blogclasses import BlogPostClass

jinja_env = setup_jinja.setup_jinja()


class NewPostHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/new-post' 
    """
    def get(self):
        error = self.request.get('error')
        title = self.request.get('title')
        content=self.request.get('content')
        titleerror = self.request.get('titleerror')
        contenterror = self.request.get('contenterror')


        t = jinja_env.get_template("new_blog_post.html")
        content = t.render(error=error, title=title, content = content, titleerror = titleerror, contenterror = contenterror)
        self.response.write(content)

    def post(self):
        new_post_title = self.request.get("post_title")
        new_post_content = self.request.get("post_content_text")
        titleerror = ""
        contenterror = ""


        # if the user typed nothing at all, redirect and yell at them
        if (not new_post_title) or (new_post_title.strip() == "") or (not new_post_content) or (new_post_content.strip() == ""):

            if (not new_post_title) or (new_post_title.strip() == ""):
                titleerror = "title fields is required."

            if (not new_post_content) or (new_post_content.strip() == ""):
                contenterror = "content field is required."

            return self.redirect("/new-post?title="
                                 + new_post_title + "&content=" + new_post_content
                                 + "&titleerror=" + titleerror + "&contenterror=" + contenterror)

        """ Adds a new blog post to the database & redirects to main page """
        blog_post = BlogPostClass.BlogPost(title = new_post_title, content = new_post_content)
        blog_post.put()

        self.redirect('/')
