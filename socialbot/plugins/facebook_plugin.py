#!/usr/bin/python
# -*- coding: utf-8 -*-

import facebook
from socialbot.utils import get_config

class FacebookPlugin(object):
    ACTION_NAME = 'Facebooked'

    def do(self, text, link):
        config = get_config()
        access_token = config.get('facebook', 'accesstoken')
        graph = facebook.GraphAPI(access_token)

        attachment =  {
            'link': link
        }
        response = graph.put_wall_post(message=text,attachment=attachment)
