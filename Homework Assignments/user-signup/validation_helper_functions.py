import cgi
import re


def empty_input(username, password, password_verify):
    if username == "":
        error_message = cgi.escape("Username cannot be blank.  Please enter a valid value.")
        return error_message
    elif password == "":
        error_message = cgi.escape("Password cannot be blank.  Please enter a valid value.")
        return error_message
    elif password_verify == "":
        error_message = cgi.escape("Password verification cannot be blank.  Please enter a valid value.")
        return error_message
    else:
        return None


def passwords_match_verification(password_user_input, password_confirm_user_input):
    if password_user_input != password_confirm_user_input:
        error_message = cgi.escape("Passwords must match.  Please try again.")
        return error_message
    else:
        return None


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
    user_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

    if user_re.match(email):
        return cgi.escape("")
    return cgi.escape("email not correct format")
