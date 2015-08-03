#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# OAuth2 Linkedin reference: https://developer.linkedin.com/docs/oauth2
#
# Steps to generate a access token
# 1) Go to linkedin and create an application
# 2) Generate a API_KEY, API_SECRET and set the RETURN_URL
# 3) run in a console: python socialbot/plugins/Linkedin_plugin.py
#    and follow the Steps
# 4) Copy the access token in the socialbot.ini file

import json

import requests

from linkedin import linkedin, server
from socialbot.utils import get_config, save_to_config

COMPANY_URL = "https://api.linkedin.com/v1/companies/{}/shares"



class Linkediner(object):
    ACTION_NAME = 'posted on Linkedin'
    def _make_request(self, method, url, token ,data=None, params=None, headers=None, timeout=60):
        headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
        params = {}
        kw = dict(data=data, params=params, headers=headers, timeout=timeout)
        params.update({'oauth2_access_token': token})
        return requests.request(method.upper(), url, **kw)

    def get_access_token(self):
        config = get_config()
        API_KEY = config.get('linkedin','api_key')
        API_SECRET = config.get('linkedin','api_secret')
        RETURN_URL = config.get('linkedin','return_url')

        permissions = ['r_basicprofile','w_share','rw_company_admin']
        authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL,permissions)
        app = linkedin.LinkedInApplication(authentication)
        print '**************************************\n'
        print '  PROCESS TO OBTAIN THE ACCESS_TOKEN  \n'
        print '**************************************\n'

        print '\nCopy and then open this URL on your browser: \n' + authentication.authorization_url
        print '\nThen login and paste the CODE \n'
        # TODO: Listen RETURN_URL parameter and look for the arg code
        # An error can ocurr, in that case, set the autorization_code variable

        authentication.authorization_code = raw_input('Input CODE: ')
        token = authentication.get_access_token()
        print '\nACCESS_TOKEN:\n ' + str(token)
        save_to_config('linkedin', 'access_token', token.access_token)
        print '\n(By default is valid for 60 days only.)'

    def submit_share(self,comment):
        config = get_config()
        access_token = config.get('linkedin','access_token')
        company_id = config.get('linkedin','company_id')
        post = {
                'comment': comment,
                'visibility': {
                    'code': 'anyone'
                }
            }
        url = COMPANY_URL.format(company_id)

        try:
            response = self.make_request('POST', url, access_token,
                                         data=json.dumps(post))
            response = response.json()
            return response
        except Exception:
            return False

    def do(self, text,link):
        body = link + " " + text
        response = self.submit_share(body)


if __name__=="__main__":
    plugin = Linkediner()
    plugin.get_access_token()
