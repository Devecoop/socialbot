# -*- coding: utf-8 -*-
# Steps to generate your token/secret credentials
# 1) After installing the requirements execute the command twitter on the cli
# 2) This will open the browser and will ask you to accept the authorization
# 3) This will create a PIN for you, you should input this in the console.
# 4) A file called .twitter_oauth will be written on your home directory, first
# line is the token, second the secret
# 5) Copy secret and token and paste them uto the appropiate section on
# socialbot.ini file

#from pyshorteners.shorteners  import Shortener
from twitter import *

from socialbot.utils import get_config

TWITTER_CONSUMER_KEY = 'uS6hO2sV6tDKIOeVjhnFnQ'
TWITTER_CONSUMER_SECRET = 'MEYTOS97VvlHX7K1rwHPEqVpTSqZ71HtvoK4sVuYk'




class Twitterer(object):
    ACTION_NAME = 'Twitted'

    def do(self, text, link):
        config = get_config()
        oauth_token = config.get('twitter', 'token')
        oauth_secret = config.get('twitter', 'secret')
        body = link + " " + text

        twitter = Twitter(
            auth=OAuth(
                oauth_token, oauth_secret,
                TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET),
            api_version='1.1',
            domain='api.twitter.com')

        twitter.statuses.update(status=body)
