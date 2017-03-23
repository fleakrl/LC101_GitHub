import webapp2

class Index(webapp2.RequestHandler):

    def get(self):
        header = """
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Flicklist</flicklist>
                </head>
                <body>
                    <h1>Flicklist</h1>

                    <h3> Edit My Watchlist </h3>

                    <form action ='/add' method = 'post'>
                        <label>
                            I would like to add:
                            <input type='text' name='new_movie'>
                            to my watchlist.
                        </label>


                </body>
            </html>
        """
        self.response.write(header)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
