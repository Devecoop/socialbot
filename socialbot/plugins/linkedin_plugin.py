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

import requests
import json

from linkedin import linkedin, server
from socialbot.utils import get_config

def make_request(method, url, token ,data=None, params=None, headers=None, timeout=60):
    headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
    params = {}
    kw = dict(data=data, params=params, headers=headers, timeout=timeout)
    params.update({'oauth2_access_token': token})
    return requests.request(method.upper(), url, **kw)


class LinkedinPlugin(object):
    ACTION_NAME = 'Linkedin-post'

    def do(self, text,link):
        body = link + " " + text
        response = self.submit_share(body)

    def doGetAccessToken(self):
        config = get_config()
        API_KEY = config.get('linkedin','api_key')
        API_SECRET = config.get('linkedin','api_secret')
        RETURN_URL = config.get('linkedin','return_url')

        permissions = ['r_basicprofile','w_share','rw_company_admin']
        authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL,permissions)
        app = linkedin.LinkedInApplication(authentication)
        print '**************************************\n'
        print 'PROCESO PARA OBTENER EL ACCESS_TOKEN \n'
        print '**************************************\n'

        print '\nCOPIAR Y ABRIR ESTA URL EN EL NAVEGADOR: \n' + authentication.authorization_url
        print '\nHACE LOGIN y copia el CODE \n'
        print 'SETEA EL CODE asi authentication.authorization_code = \'<poner code aca>\'  \n'
        #print authenticatio.access_url
        import pdb; pdb.set_trace()
        token = authentication.get_access_token()
        print '\nEl ACCESS_TOKEN:\n ' + str(token)
        print '\n(Por default tiene validez por 60 dias)'

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
        url = 'https://api.linkedin.com/v1/companies/'+COMPANY_ID+'/shares'
        try:
            response = make_request('POST', url, ACCESS_TOKEN,data=json.dumps(post))
            response = response.json()
            return response
        except Exception:
            return False

if __name__=="__main__":
    plugin = LinkedinPlugin()
    plugin.doGetAccessToken()
