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


def build_page(error=""):
    heading = "<h1>User Signup</h1>"
    username_label = "<label>Username: </label>"
    username_input = "<input type = 'text' name = 'username'/>"
    password_label = "<label>Password: </label>"
    password_input = "<input type = 'password' name = 'password'/>"
    password_verify_label = "<label>Verify Password: </label>"
    password_verify_input = "<input type = 'password' name = 'password_verify'/>"
    email_label = "<label>Email (optional): </label>"
    email_input = "<input type = 'text' name = 'email'/>"

    submit = "<input type = submit />"

    error_messages = "<div style='color: red'> %(errors)s </div>"

    form = (
            "<form method = 'post'>" + username_label + username_input + "<p/>" + password_label +
            password_input + "<p/>" + password_verify_label + password_verify_input +
            "<p/>" + email_label + email_input + "<p/>" + submit
            )

    return heading + form, error

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page()
        self.response.write(content[0] % {"error": content[1]})

    def post(self):
        username = cgi.escape(self.request.get('username'))
        email = cgi.escape(self.request.get('email'))
        self.response.write("thanks for submitting!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)