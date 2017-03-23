import webapp2

header = """
<!DOCTYPE html>
<html>

<head>
    <title>Flicklist</title>
</head>

<body>
    <h1>Flicklist</h1>
"""
footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):

    def get(self):
        form = """
          <h3> Edit My Watchlist </h3>

          <form action ='/add' method = 'post'>
            <label> I would like to add
                <input type='text' name='new_movie'/>
                to my watchlist.
            </label>
            <input type = 'submit' value = 'Add it'>
         </form>
        """
        self.response.write(header + form + footer)

class AddMovie(webapp2.RequestHandler):

    def post(self):
        movie_name = self.request.get('new_movie')

        success_message = "<strong>" + movie_name + "</strong> has been added to your list. (but not really)"

        self.response.write(header + success_message+ footer)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
