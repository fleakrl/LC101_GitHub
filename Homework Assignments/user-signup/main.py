import webapp2
import cgi
import helper_functions


class MainHandler(webapp2.RequestHandler):

    def get(self):
        # build the form
        self.response.write(helper_functions.build_form())

    def post(self):
        # store the escaped user inputs
        username = cgi.escape(self.request.get('username'))
        password = cgi.escape(self.request.get('password'))
        password_verify = cgi.escape(self.request.get('password_verify'))
        email = cgi.escape(self.request.get('email'))

        # validate the user inputs
        username_error = helper_functions.validate_username(username)
        password_error = helper_functions.validate_password(password)
        password_verify_error = helper_functions.validate_password_verify(password_verify, password)
        email_error = helper_functions.validate_email(email)

        # if user inputs are valid redirect to acceptance page
        if username_error == "" and password_error == "" and password_verify_error == "" and email_error == "":
            self.redirect('/accepted')

        # if user inputs are not valid, respond by rebuilding the form with error messages
        self.response.out.write(helper_functions.build_form(username_error, password_error,
                                                            password_verify_error, email_error, username, email))


class Acceptance(webapp2.RequestHandler):
    def get(self):
        header = "<h1>User Signup Confirmed</h1>"
        content = header + "Thanks for submitting!"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/accepted',Acceptance)
], debug=True)
