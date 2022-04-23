#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Must start this script with an axe, a tinderbox and runes
# for high alching and camelot teleport, you must also be on max brightness and
# be zoomed out to max

from pylibsythe import *
import sythelib_utils as utils
import sythelib_utils
import random

pylibsythe.set_human_mouse_mode_on
set_virtual_inputs_off()
pylibsythe.set_mouse_delay(273, 352) #random delays on mouse movements
tree_color = 0xA400FF

USERNAME = ("")
PASSWORD = ("")

utils.start("OpenOSRS")  # change this to the client you play on
utils.login(USERNAME, PASSWORD, utils.FONTS)

sleep(3000) # time to get ready

def list_of_antiban():

    while True:  # looper

        if random.random() < 0.031:  # chance of proc
            pylibsythe.key_down(0x25)  # press left arrow key down for antiban
            sleep(random.randint(200, 4875))  # random values for delay
            pylibsythe.key_up(0x25)  # lift left arrow key down for antiban

        if random.random() < 0.033:  # chance of proc
            pylibsythe.key_down(0x27)  # press right arrow key down for antiban
            sleep(random.randint(220, 2576))  # random values for delay
            pylibsythe.key_up(0x27)  # lift right arrow key up for antiban

        if random.random() < 0.023:  # chance of proc
            pylibsythe.key_down(0x26)  # press up arrow key down for antiban
            sleep(random.randint(150, 3009))  # random values for delay
            pylibsythe.key_up(0x26)  # lift up arrow key up for antiban

        if random.random() < 0.073:  # chance of proc
            pylibsythe.key_down(0x28)  # press down arrow key down for antiban
            sleep(random.randint(100, 8653))  # random values for delay
            pylibsythe.key_up(0x28)  # lift down arrow key up for antiban

        if random.random() < 0.017:  # chance of proc
            pylibsythe.click_mouse_random_area(170, 150, 290, 325, 1)  # run around for antiban

        if random.random() < 0.053:  # chance of proc
            pylibsythe.key_down(0x71)  # presses F2 to change to skill menu
            sleep(random.randint(34, 178))  # random values for delay
            pylibsythe.key_up(0x71)  # lifts F2 to change to skill menu
            sythelib_utils.custom_mouse.random_move_mouse(578, 381)  # Exp check for antiban
            sleep(random.randint(1356, 7863))  # random values for delay

        if random.random() < 0.054:  # chance of proc
            while found_tree := get_poly_point(tree_color):
                utils.random_click_mouse(found_tree.x, found_tree.y)
                sleep(random.randint(5073, 8567)) # allows time for a log to be cut
                pylibsythe.key_down(0x1B)  # presses ESC to open the inventory
                sleep(random.randint(34, 78))  # random values for delay
                pylibsythe.key_up(0x1B)  # lifts ESC
                utils.click_random_bitmap_point(utils.ITEMS.tinderbox()) # burns a log
                sleep(random.randint(34, 78))  # random values for delay
                utils.click_random_bitmap_point(utils.ITEMS.logs())
                sleep(random.randint(8734, 12654))  # waits for fire to burn
            scrape()

        main()

def main():

    while True: # looper

        pylibsythe.antigcp()  # checks if client is in foreground.background

        pylibsythe.key_down(0x75)  # clicks on spellbook

        utils.click_random_circle_point(700, 290, 1, 8) # clicks on camelot teleport
        sleep(random.randint(2000, 3000)) # sleeps for enough time to allow another teleport

        if get_async_key_state(0x1B):
            print("Program exited successfully")
            exit()

        list_of_antiban()

main();

