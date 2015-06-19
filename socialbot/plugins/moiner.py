#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from MoinMoin.web.contexts import ScriptContext
from MoinMoin.Page import Page
from MoinMoin.PageEditor import PageEditor
from MoinMoin import search
import MoinMoin.user
from twitter import *                                                               

from socialbot.utils import get_config


class Moiner(object):
    ACTION_NAME = 'Wikied'

    def do(self, text):
        import MoinMoin.user
        from MoinMoin.PageEditor import PageEditor
        from MoinMoin.web.contexts import ScriptContext

        config = get_config()
        user_email = config.get('moiner', 'user_email')

        request = ScriptContext()
        user = MoinMoin.user.get_by_email_address(request,
                                                 user_email)
        request.user = user
        pe = PageEditor(request, 'Links')
        text = pe.get_raw_body() + "\n" + pe.normalizeText(text)
        dummy, revision, exists = pe.get_rev()
        pe.saveText(text, revision)
