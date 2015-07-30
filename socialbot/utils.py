#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from ConfigParser import SafeConfigParser


def get_config():
    user_home = os.path.expanduser("~")
    config_file_path = os.path.join(user_home, '.config', 'socialbot', 'socialbot.ini')

    config = SafeConfigParser()
    config.read(config_file_path)

    return config


def save_to_config(section, option, value):
    user_home = os.path.expanduser("~")
    config_file_path = os.path.join(user_home, '.config', 'socialbot', 'socialbot.ini')

    config = SafeConfigParser()
    config.read(config_file_path)

    #If the section does not exist create a new one
    if section not in config.sections():
        config.add_section(section)

    config.set(section, option, str(value))
    with open(config_file_path, 'wb') as cf:
        config.write(cf)
