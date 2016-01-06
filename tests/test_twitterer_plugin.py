#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_socialbot
----------------------------------

Tests for `socialbot` module.
"""

import unittest

from socialbot.plugins.twitterer import Twitterer


class TestTwittererPlugin(unittest.TestCase):

    def test_validate_characters_above_140_max(self):
        body = "link" + "long" * 50
        self.assertRaises(Exception, Twitterer().validate, body)

    def test_validate_characters_below_140_max(self):
        self.assertTrue(Twitterer().validate("link", "small ok"))

if __name__ == '__main__':
    unittest.main()
