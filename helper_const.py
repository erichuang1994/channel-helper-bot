#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Channel Helper Bot """
""" helper_const.py """
""" Copyright 2018, Jogle Lew """
import os

BOT_TOKEN = os.environ['TOKEN']
BOT_OWNER = [os.environ['OWNERID']]
MIN_REFRESH_INTERVAL = 3
MODULE_NAME = ['start_cmd', 'help_cmd', 'cancel_cmd', 'sql_cmd', 'clean_cmd', 'register_cmd', 'option_cmd', 'channel_msg', 'private_msg', 'callback_query', 'inline_query']
DATABASE_DIR = os.environ['DB'] if os.environ['DB'] else "."
DEFAULT_LANG = "zh-CN"
LANG_LIST = ["zh-CN", "pt-BR", "en-US"]
LANG_WIDTH = 3
DEFAULT_BUTTONS = ["👍", "👎"]
