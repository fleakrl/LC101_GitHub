import cgi


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
