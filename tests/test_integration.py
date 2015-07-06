#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_socialbot
----------------------------------

Tests for `socialbot` module.
"""

import json
import unittest

import requests

from socialbot.main import SlackBotHandler
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class TestSocialbot(unittest.TestCase):
    def test_integration_valid_url_with_text(self):
        result = requests.post('http://127.0.0.1:3001', 
                               {'user_name':'ska', 
                               'text':'wikisave <http://wwww.lanux.org.ar> Lolo'})
        parsed_result = json.loads(result.content).get("text")
        self.assertTrue(parsed_result.find("Thanks")!=-1)

    def test_integration_valid_url_no_http(self):
        result = requests.post('http://127.0.0.1:3001', 
                               {'user_name':'ska', 
                               'text':'wikisave <http://wwww.lanux.org.ar|lanux.org.ar> Lolo'})
        parsed_result = json.loads(result.content).get("text")
        self.assertTrue(parsed_result.find("Sorry")!=-1)

    def test_integration_invalid_url_no_http_no_text(self):
        result = requests.post('http://127.0.0.1:3001', 
                               {'user_name':'ska', 
                               'text':'wikisave lala.vom Lolo'})
        parsed_result = json.loads(result.content).get("text")
        self.assertTrue(parsed_result.find("Sorry")!=-1)

if __name__ == '__main__':
    unittest.main()
