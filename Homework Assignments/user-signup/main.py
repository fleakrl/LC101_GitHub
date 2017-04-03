#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import validation_helper_functions
page_header = """
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
"""

page_footer = """
</body>
</html>
"""

def build_page(username_from_user, email):
    heading = "<h1>User Signup</h1>"
    username_label = "<label>Username: </label>"
    username_input = "<input type = 'text' name = 'username' value = '{0}'/>".format(username_from_user)
    password_label = "<label>Password: </label>"
    password_input = "<input type = 'password' name = 'password'/>"
    password_verify_label = "<label>Verify Password: </label>"
    password_verify_input = "<input type = 'password' name = 'password_verify'/>"
    email_label = "<label>Email (optional): </label>"
    email_input = "<input type = 'text' name = 'email' value = '{0}'/>".format(email)

    submit = "<input type = submit />"

    form = (
            "<form method = 'post'>" + username_label + username_input + "<p/>" + password_label +
            password_input + "<p/>" + password_verify_label + password_verify_input +
            "<p/>" + email_label + email_input + "<p/>" + submit
            )

    return heading + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        username_from_user = self.request.get("username")
        email = self.request.get("email")

        error = self.request.get("error")

        error_msg = ""
        if error:
            error_msg = "<div>" + error + "</div>"
            username_from_user = self.request.get("username")
            email = self.request.get("email")

        content = build_page(username_from_user, email)

        self.response.write(page_header + content + error_msg + page_footer)

    def post(self):
        username = cgi.escape(self.request.get('username'))
        password = cgi.escape(self.request.get('password'))
        password_verify = cgi.escape(self.request.get('password_verify'))
        email = cgi.escape(self.request.get('email'))
        self.response.write("thanks for submitting!")

        # make sure user input is not empty
        if validation_helper_functions.empty_input(username, password, password_verify) is not None:
            error_message ="<p class = 'error'>" +\
                           validation_helper_functions.empty_input(username, password, password_verify) +\
                           "</p>"
            self.redirect("/?error=" + error_message)

        # make sure password and password confirm match
        if validation_helper_functions.passwords_match_verification(password,password_verify) is not None:
            error_message = "<p class = 'error'>" + \
                            validation_helper_functions.passwords_match_verification(password,password_verify) +\
                            "</p>"
            self.redirect("/?error=" + error_message, "/?username=" + username, "/?email=" + email)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
