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
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(username)


def validate_password(password):
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(password)


def validate_email(email):
    user_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    return user_re.match(email)
