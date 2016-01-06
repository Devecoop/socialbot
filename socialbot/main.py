#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from socialbot.utils import get_config

config = get_config()
MAGIC_KEYWORD = config.get('main', 'magic_keyword')


class SlackBotHandler(BaseHTTPRequestHandler):

    def _check_is_valid(self, url):
        return True

    def _sanitize(self, url):
        return url

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        payload = None
        user_name = None
        try:
            postvars = cgi.parse_qs(post_body, keep_blank_values=1)
            user_name = postvars.get('user_name')[0]
            content = postvars.get('text')[0]
            has_pipe = content.find("|")
            has_less = content.find("<")
            if has_pipe != -1 or has_less == -1:
                raise Exception("Invalid Link format")

            raw_link = content.strip("{} <".format(MAGIC_KEYWORD))
            link, text = raw_link.split(">")

            map(lambda x: x.validate(text, link), self.plugin_list)

            # TODO: Change this, so it can return an status for each of
            # the actions
            map(lambda x: x.do(text, link), self.plugin_list)

            actions = [k.ACTION_NAME for k in self.plugin_list]
            action_string = " and ".join(actions)

            payload = '{"text" : "Thanks for the link, %s. It has been %s "}' % (user_name, action_string)
        except Exception as err:
            payload = '{"text" : "Sorry %s! Could not process message. (%s)"}' % (user_name, str(err))
        finally:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write(payload)

        return

if __name__ == '__main__':
    try:
        #Create a web server and define the handler to manage the
        #incoming request
        config = get_config()
        PORT_NUMBER = int(config.get('main', 'port'))
        # TODO: Read this from config file and import them accordingly
        from socialbot.plugins.twitterer import Twitterer
        from socialbot.plugins.relayer import Relayer
        from socialbot.plugins.facebooker import Facebooker
        from socialbot.plugins.linkediner import Linkediner
        plugin_list = [
            Relayer(),
            Twitterer(),
            Linkediner(),
            #Facebooker(),
        ]
        SlackBotHandler.plugin_list = plugin_list
        server = HTTPServer(('', PORT_NUMBER), SlackBotHandler)
        print 'Started httpserver on port ', PORT_NUMBER
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
