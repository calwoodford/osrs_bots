#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pylibsythe import *
import sythelib_utils as utils

utils.start("OpenOSRS")

willow_color = 0xFFFF00
chopping_area = 11, 26, 133, 72
0
scrape()
while found_tree := get_poly_point(willow_color):
    if find_color(0xFF0000, *chopping_area):  # if it's red and not chopping
        utils.random_click_mouse(found_tree.x, found_tree.y)
        sleep(3_000)
    if utils.is_inventory_full():
        utils.drop_item(items.willow_logs())
    scrape()

    if get_async_key_state(0x71):
        exit()
