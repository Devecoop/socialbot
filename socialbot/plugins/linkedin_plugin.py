#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from linkedin import linkedin

from socialbot.utils import get_config

API_KEY = '77z1yvd5t5upb6'
API_SECRET = 'IlVYmc1vysepzZh7'
RETURN_URL = 'https://devecoop.slack.com/'


class Twitterer(object):
    ACTION_NAME = 'Linkedin-post'

    def do(self, text, link):
        config = get_config()
        authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
        application = linkedin.LinkedInApplication(authentication)

        json.shareObj({'comment':  str(text)+str(link), 'visibility': {'code': 'anyone' }})

        application.submit_share(json.shareObj)
