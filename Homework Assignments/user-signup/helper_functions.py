import cgi
import re


def build_form(username_error="", password_error="", password_verify_error="", email_error=""):
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
            <h1> User Signup </h1>
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
    """ % (username_error, password_error, password_verify_error, email_error))


def validate_username(username):
    if username == "":
        return cgi.escape("Username cannot be blank.")
    else:
        user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        if user_re.match(username):
            return cgi.escape("")
        else:
            return cgi.escape("Username not correct format.")


def validate_password(password):
    if password == "":
        return cgi.escape("Password cannot be blank.")
    else:
        user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        if user_re.match(password):
            return cgi.escape("")
        else:
            return cgi.escape("Password not correct format")


def validate_password_verify(password_verify, password):
    if password_verify == "":
        return cgi.escape("Password Verify cannot be blank")
    else:
        if password_verify == password:
            return cgi.escape("")
        else:
            return cgi.escape("Password and password verify must match")


def validate_email(email):
    if email == "":
        return ""
    else:
        user_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

        if user_re.match(email):
            return cgi.escape("")
        return cgi.escape("email not correct format")
