#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from socialbot.utils import get_config


class Relayer(object):
    ACTION_NAME = 'Posted'

    def do(self, text, link):
        config = get_config()
        relayer = config.get('relayer', 'url')
        username = config.get('relayer', 'username')
        result =  requests.post(relayer,
		     {"user_name": username,
                      "text": text, "link":link})
        return("OK")
