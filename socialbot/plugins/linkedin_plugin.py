#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from linkedin import linkedin, server

from socialbot.utils import get_config

RETURN_URL = 'https://devecoop.slack.com/'
API_KEY = '776fdrbu36uot9'
API_SECRET = 'IUKB8MvRpd54AJuK'


class LinkedinPlugin(object):
    ACTION_NAME = 'Linkedin-post'

    def do(self, text, link):
        config = get_config()

        #authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
        #application = linkedin.LinkedInApplication(authentication)
        application = server.quick_api(API_KEY, API_SECRET)

        application.get_profile()
        #json.shareObj({'comment':  str(text)+str(link), 'visibility': {'code': 'anyone' }})

        #application.submit_share(json.shareObj)

if __name__=="__main__":
    plugin = LinkedinPlugin()
    plugin.do("text", "link")
