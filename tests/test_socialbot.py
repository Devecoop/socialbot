#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_socialbot
----------------------------------

Tests for `socialbot` module.
"""

import unittest
import threading

import requests

from socialbot.main import SlackBotHandler
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from socialbot.plugins.facebook_plugin import FacebookPlugin

class TestSocialbot(unittest.TestCase):
    def setUp(self):
        print('---- setup start')
        self.httpd = HTTPServer(('', 8081), SlackBotHandler)

        print('---- setting plugins')
        SlackBotHandler.plugin_list = [FacebookPlugin()]

        threading.Thread(target=self.serve).start()
        print('---- setup complete')

    def serve(self):
        try:
            self.httpd.serve_forever()
        finally:
            self.httpd.server_close()

    def tearDown(self):
        print('---- teardown start')
        self.httpd.shutdown()
        print('---- teardown complete')

    def test1(self):
        print('---- test1 start')
        print(threading.current_thread())
        result = requests.post('http://127.0.0.1:8081', {'user_name':'ska', 'text':'wikisave <http://wwww.lanux.org.ar> este es otro texto largo'})
        print result
        print('---- test1 complete')

if __name__ == '__main__':
    unittest.main()
