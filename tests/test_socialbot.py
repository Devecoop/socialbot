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


class TestSocialbot(unittest.TestCase):
    def setUp(self):
        print('---- setup start')
        self.httpd = HTTPServer(('', 8081), SlackBotHandler)
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

    def _test1(self):
        print('---- test1 start')
        print(threading.current_thread())
        result = requests.post('http://127.0.0.1:8080', {'user_name':'ska', 'text':'wikisave <http://wwww.lanux.org.ar> Lolo'})
        print result
        print('---- test1 complete')

if __name__ == '__main__':
    unittest.main()
