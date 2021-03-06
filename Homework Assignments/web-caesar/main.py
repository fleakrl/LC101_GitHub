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
import caesar
import cgi


def build_page(textarea_content):
    # website formatting

    heading = "<h1> Welcome to Web Caesar </h1>"
    rotation_label = "<label> Rotate by: </label>"
    rotation_input = "<input type = 'number' name = 'rotation'/>"

    message_label = "<label>Please input a message to encrypt:</label><p/>"
    textarea = "<textarea name = 'message'>" + textarea_content + "</textarea>"
    submit = "<input type = submit />"

    footer = "<footer> <p>Created By: Rebecca Fleak</p><p>&copy March 2017</p>"

    form = ("<form method = 'post'>" + "<p>" + rotation_label + rotation_input
            + "</p>" + message_label + textarea + "</p>" + submit + footer + "</form>")

    return heading + form

class MainHandler(webapp2.RequestHandler):

    def get(self):

        content = build_page("")
        self.response.write(content)

    def post(self):
        # Section for the actual encryption
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
