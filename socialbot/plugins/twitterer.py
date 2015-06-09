#!/usr/bin/python
# -*- coding: utf-8 -*-
from twitter import *

from socialbot import get_config

TWITTER_CONSUMER_KEY = 'uS6hO2sV6tDKIOeVjhnFnQ'
TWITTER_CONSUMER_SECRET = 'MEYTOS97VvlHX7K1rwHPEqVpTSqZ71HtvoK4sVuYk'


class Twitterer(object):
    ACTION_NAME = 'Twitted'

    def do(self, text):
        config = get_config()
        oauth_token = config.get('twitter', 'token')
        oauth_secret = config.get('twitter', 'secret')

        twitter = Twitter(
            auth=OAuth(
                oauth_token, oauth_secret,
                TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET),
            api_version='1.1',
            domain='api.twitter.com')

        twitter.statuses.update(status=text)
