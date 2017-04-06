import webapp2
import cgi
import validation_helper_functions

def build_form(username_error = "", password_error = "", password_verify_error = "", email_error = ""):
    return str("""
    <!DOCTYPE html>
    <html>
        <head>
            <title>User Signup</title>
            <style type="text/css">
                .error {
                    color: red;
                }
            </style>
        </head>
        <body>
            <form method = "post">
                <table>
                    <tr>
                        <td><label>Username:</label></td>
                        <td><input type="text" name="username" required/></td>
                        <td><span class="error">%s</span></td>
                    </tr>
                    <tr>
                        <td><label>Password:</label></td>
                        <td><input type="password" name="password" required/></td>
                        <td><span class="error">%s</span></td>
                    </tr>
                    <tr>
                        <td><label>Password Verify:</label></td>
                        <td><input type="password" name="password_verify" required/></td>
                        <td><span class="error">%s</span></td>
                    </tr>
                    <tr>
                        <td><label>Email (Optional):</label></td>
                        <td><input type="text" name="email"/></td>
                        <td><span class="error">%s</span></td>
                    </tr>
                </table>
                
                <input type = submit />
            </form>
        
        </body>
    </html>
    """
    % (username_error, password_error, password_verify_error, email_error))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write(build_form())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
