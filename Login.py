#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pylibsythe import *
import sythelib_utils as utils

USERNAME = ""
PASSWORD = ""

sleep(5000)
utils.start("OpenOSRS")  # change this to the client you play on
utils.login(USERNAME, PASSWORD, utils.FONTS)
