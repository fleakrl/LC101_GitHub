import webapp2

movie_list = [
            "Beauty and the Beast",
            "Little Mermaid",
            "Lion King",
            "Snow White and the Seven Dwarfs",
            "Cinderella"
        ]

def generate_current_movie_list():
    print_movie_list = "<h3> Current Movie List</h3>"
    for index in range(len(movie_list)):
        print_movie_list += str(movie_list[index]) + "<br>"

    return print_movie_list

def generate_dropdown():

    option_open = "<option>"
    option_close = "</option>"

    dropdown = "<select name = select_movie>"

    for index in range(len(movie_list)):
        dropdown += option_open + movie_list[index] + option_close

    dropdown += "</select>"
    return dropdown



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
         <br>
         <form action ='/crossoff' method = 'post'>
            <label> I would like to cross off """ + generate_dropdown() + """
                on my watchlist.
            </label>
            <input type = 'submit' value = 'cross it'>
         </form>
         <form action ='/delete' method = 'post'>
            <label> I would like to remove  """ + generate_dropdown() + """
                from my watchlist.
            </label>
            <input type = 'submit' value = 'cross it'>
         </form>
        """


        self.response.write(header + form + generate_current_movie_list() +footer)


class AddMovie(webapp2.RequestHandler):

    def post(self):
        movie_name = self.request.get('new_movie')

        success_message = "<strong>" + movie_name + "</strong> has been added to your list. <br><br>"

        movie_list.append(movie_name)



        self.response.write(header + success_message + generate_current_movie_list() + footer)


class CrossOffMovie(webapp2.RequestHandler):
    def post(self):
        movie_name = "<strike>" + self.request.get('select_movie') + "</strike>"

        return_message = movie_name + " has been crossed off your watchlist."

        self.response.write(header + return_message + footer)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/crossoff',CrossOffMovie)
], debug=True)
