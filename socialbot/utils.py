#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from ConfigParser import SafeConfigParser


def get_config():
    user_home = os.path.expanduser("~")
    config_file_path = os.path.join(user_home, '.config', 'socialbot.ini')

    config = SafeConfigParser()
    config.read(config_file_path)

    return config
