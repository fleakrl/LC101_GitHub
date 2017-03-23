import webapp2
from random import randint

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movie_list = [
            "Beauty and the Beast",
            "Little Mermaid",
            "Lion King",
            "Snow White and the Seven Dwarfs",
            "Cinderella"
        ]

        # TODO: randomly choose one of the movies, and return it
        movie_selection = movie_list[randint(0, len(movie_list) - 1)]

        return movie_selection

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        new_movie_selection = movie

        while new_movie_selection == movie:
            new_movie_selection = self.getRandomMovie()

        content += "<h1>Tomorrow's Movie</h1>"
        content += new_movie_selection

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
