# Must be at max brightness and have inventory key set to F11
# Must have logout menu key set to F5
# Must be zoomed to around the default OSRS level
# Turn auto-retaliate on
# Start with inventory open and run energy on
# There's an error that occurs when no enemies can be found
# Try to go to an unpopulated world
# Turn ESC closes window on in OSRS keybindings
# Ideally have a scimitar equipped
# The Opponent Information and NPC Indicator plugins are required
# Change the wait time in the main function depending on your level so it's not waiting for too long or
# moving too quickly
# Make sure to occasionally do a quest or train another skill for optimal antiban
# I imagine doing Stronghold of Security and adding two factor authentication helps
# Be a member/train in member zones and worlds
# Must have 25 Magic and Varrock teleport runes


# TODO search for 'I can't reach that' bitmap and logout if it's seen more than 4 times for example
# TODO search for random event text, right click the bitmap randomly and dismiss
# TODO click the text when a new level arrives
# TODO find out how to stop the mouse going to 1,1 at the start
# TODO find out how to use the scroll wheel for quest and music scrolling
# TODO attack another enemy when the bitmap 'Someone else is fighting that' appears
# TODO Pressing ESC to exit the script no longer works for some reason - need to figure this out
# TODO Learn how to do 'if this exists in inventory - click it' for big bones
# TODO Learn how to do 'if this exists in inventory - click it' for big bones


from pylibsythe import *
import sythelib_utils as utils
import random

set_virtual_inputs_off()
pylibsythe.set_human_mouse_mode_on()

utils.start("OpenOSRS")
print("Get ready...")
sleep(random.randint(3000, 6578))  # time to get ready

THRESHOLD = 15  # eats if under this threshold
TELEPORT_THRESHOLD = 6  # eats if under this threshold
npc_color = 0xFF00F1  # change this to the color you want
combat_color = 0x0A8633
combat_area = 5, 3, 12, 66
npc_name = "Chaos druid"  # change this to the mob name
pylibsythe.set_mouse_delay(517, 357)

USERNAME = "username"
PASSWORD = "password"

utils.custom_mouse.MouseMovementCalculator(5, 7, 60073, 321)


def list_of_antiban():
    scrape()
    if utils.get_health(utils.FONTS.font3) < TELEPORT_THRESHOLD:  # teleports to safety and ends if you run out of food
        pylibsythe.key_down(0x75)  # clicks on spellbook
        utils.click_random_circle_point(596, 263, 1, 8)  # clicks on varrock teleport
        sleep(random.randint(556, 768))
        pylibsythe.key_down(0x74)  # press logout menu
        sleep(random.randint(310, 875))  # random values for delay
        pylibsythe.key_up(0x74)  # lift logout menu
        sleep(random.randint(10170, 13578))  # sleep for 10-13 seconds approx after combat to logout
        utils.utils.click_random_square_point(580, 415, 165, 30, 1)  # click logout
        exit()

    # generic pause
    if random.random() < 0.036:  # chance of proc
        print("brief pause")
        sleep(random.randint(15732, 31645))

    # generic pause
    if random.random() < 0.014:  # chance of proc
        print("brief pause")
        sleep(random.randint(25792, 37685))

    if random.random() < 0.091:  # chance of proc
        print("running antiban")
        pylibsythe.key_down(0x25)  # press left arrow key down for antiban
        sleep(random.randint(200, 4875))  # random values for delay
        pylibsythe.key_up(0x25)  # lift left arrow key down for antiban

    if random.random() < 0.099:  # chance of proc
        print("running antiban")
        pylibsythe.key_down(0x27)  # press right arrow key down for antiban
        sleep(random.randint(220, 2576))  # random values for delay
        pylibsythe.key_up(0x27)  # lift right arrow key up for antiban

    if random.random() < 0.093:  # chance of proc
        print("running antiban")
        pylibsythe.key_down(0x26)  # press up arrow key down for antiban
        sleep(random.randint(150, 3009))  # random values for delay
        pylibsythe.key_up(0x26)  # lift up arrow key up for antiban

    if random.random() < 0.072:  # chance of proc
        print("running antiban")
        pylibsythe.key_down(0x28)  # press down arrow key down for antiban
        sleep(random.randint(100, 8653))  # random values for delay
        pylibsythe.key_up(0x28)  # lift down arrow key up for antiban

    if random.random() < 0.017:  # down and right arrows at the same time
        print("running antiban")
        pylibsythe.key_down(0x28)  # press down arrow key down for antiban
        pylibsythe.key_down(0x27)  # press right arrow key down for antiban
        sleep(random.randint(100, 8653))  # random values for delay
        pylibsythe.key_up(0x28)  # lift down arrow key up for antiban
        sleep(random.randint(100, 8653))  # random values for delay
        pylibsythe.key_up(0x27)  # lift right arrow key up for antiban
        sleep(random.randint(220, 2576))  # random values for delay

    if random.random() < 0.077:  # down and left arrows at the same time
        print("running antiban")
        pylibsythe.key_down(0x28)  # press down arrow key down for antiban
        pylibsythe.key_down(0x25)  # press left arrow key down for antiban
        sleep(random.randint(100, 3453))  # random values for delay
        pylibsythe.key_up(0x28)  # lift down arrow key up for antiban
        sleep(random.randint(100, 6853))  # random values for delay
        pylibsythe.key_up(0x25)  # lift left arrow key up for antiban
        sleep(random.randint(120, 1276))  # random values for delay

    if random.random() < 0.037:  # up and right arrows at the same time
        print("running antiban")
        pylibsythe.key_down(0x26)  # press up arrow key down for antiban
        pylibsythe.key_down(0x27)  # press right arrow key down for antiban
        sleep(random.randint(100, 2253))  # random values for delay
        pylibsythe.key_up(0x26)  # lift up arrow key up for antiban
        sleep(random.randint(67, 3351))  # random values for delay
        pylibsythe.key_up(0x27)  # lift right arrow key up for antiban
        sleep(random.randint(287, 2176))  # random values for delay

    if random.random() < 0.085:  # up and left arrows at the same time
        print("running antiban")
        pylibsythe.key_down(0x26)  # press up arrow key down for antiban
        pylibsythe.key_down(0x25)  # press left arrow key down for antiban
        sleep(random.randint(108, 2953))  # random values for delay
        pylibsythe.key_up(0x26)  # lift up arrow key up for antiban
        sleep(random.randint(100, 4553))  # random values for delay
        pylibsythe.key_up(0x25)  # lift left arrow key up for antiban
        sleep(random.randint(127, 276))  # random values for delay

    if random.random() < 0.071:  # chance of proc
        print("running antiban")
        pylibsythe.key_down(0x28)  # press down arrow key down for antiban
        sleep(random.randint(97, 106))  # random values for delay
        pylibsythe.click_mouse_random_area(170, 150, 290, 325, 2)  # run around for antiban
        sleep(random.randint(93, 97))
        pylibsythe.click_mouse_random_area(170, 150, 290, 325, 1)  # run around for antiban
        pylibsythe.key_up(0x28)  # lift down arrow key up for antiban

    if random.random() < 0.017:  # chance of proc
        print("running antiban")
        sleep(random.randint(43, 107))
        pylibsythe.click_mouse_random_area(170, 150, 290, 325, 1)  # run around for antiban
        sleep(random.randint(63, 87))

    if random.random() < 0.011:  # chance of proc
        print("running antiban")
        sleep(random.randint(53, 107))
        pylibsythe.click_mouse_random_area(1, 1, 510, 320, 1)  # run around for antiban
        sleep(random.randint(59, 157))

    if random.random() < 0.008:  # chance of proc
        print("running antiban")
        sleep(random.randint(99, 137))
        pylibsythe.click_mouse_random_area(1, 1, 510, 320, 2)  # right click for antiban
        sleep(random.randint(79, 167))

    # dragging and turning around for antiban using the middle mouse button
    if random.random() < 0.009:  # chance of proc
        print("running antiban")
        pylibsythe.key_down(0x04)  # press down arrow key down for antiban
        pylibsythe.click_mouse_random_area(170, 150, 290, 325, 2)
        sleep(random.randint(100, 8653))  # random values for delay
        pylibsythe.key_up(0x04)  # lift down arrow key up for antiban
        sleep(random.randint(192, 197))  # random values for delay
        pylibsythe.key_down(0x26)  # press up arrow key down for antiban
        sleep(random.randint(192, 197))  # random values for delay
        pylibsythe.key_up(0x26)  # lift up arrow key up for antiban
        sleep(random.randint(192, 197))  # random values for delay
        pylibsythe.key_down(0x25)  # press left arrow key down for antiban
        sleep(random.randint(93, 735))  # random values for delay
        pylibsythe.click_mouse_random_area(170, 150, 290, 325, 3)
        sleep(random.randint(87, 99))
        pylibsythe.click_mouse_random_area(170, 150, 290, 325, 2)
        pylibsythe.key_up(0x25)  # lift left arrow key down for antiban\

    if random.random() < 0.0082:  # chance of proc - this is a random right click in inventory or panel
        sleep(random.randint(33, 65))  # random values for delay
        utils.click_random_circle_point(650, 300, 2, 50)
        sleep(random.randint(93, 765))  # random values for delay

    if random.random() < 0.008:  # skill check
        pylibsythe.key_down(0x71)  # press F2
        sleep(random.randint(257, 878))  # random values for delay
        pylibsythe.key_up(0x71)  # release F2
        sleep(random.randint(373, 1215))  # waits for mouse to get to skill
        utils.utils.click_random_square_point(555, 205, 200, 160, 0)  # hover
        sleep(random.randint(973, 1295))  # waits for mouse to get to skill
        pylibsythe.key_down(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(241, 297))  # random values for delay
        pylibsythe.key_up(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(71, 137))  # random values for delay

    if random.random() < 0.003:  # double skill check
        pylibsythe.key_down(0x71)  # press F2
        sleep(random.randint(257, 878))  # random values for delay
        pylibsythe.key_up(0x71)  # release F2
        sleep(random.randint(373, 1215))  # waits for mouse to get to skill
        utils.utils.click_random_square_point(555, 205, 200, 160, 0)  # hover
        sleep(random.randint(1073, 1595))  # waits for mouse to get to skill
        utils.utils.click_random_square_point(555, 205, 200, 160, 0)  # hover
        sleep(random.randint(573, 1795))  # waits for mouse to get to skill
        pylibsythe.key_down(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(241, 297))  # random values for delay
        pylibsythe.key_up(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(71, 137))  # random values for delay

    if random.random() < 0.033:  # combat level check
        pylibsythe.key_down(0x70)  # press F1
        sleep(random.randint(70, 845))  # random values for delay
        pylibsythe.key_up(0x70)  # release F1
        sleep(random.randint(470, 845))  # random values for delay
        pylibsythe.key_down(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(71, 139))  # random values for delay
        pylibsythe.key_up(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(61, 127))  # random values for delay

    if random.random() < 0.013:  # worn equipment check
        pylibsythe.key_down(0x73)  # press F4
        sleep(random.randint(50, 1145))  # random values for delay
        pylibsythe.key_up(0x73)  # release F4
        sleep(random.randint(173, 395))  # random values for delay
        pylibsythe.key_down(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(91, 119))  # random values for delay
        pylibsythe.key_up(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(87, 177))  # random values for delay

    if random.random() < 0.0071:  # worn equipment check and check stats
        pylibsythe.key_down(0x73)  # press F4
        sleep(random.randint(50, 1145))  # random values for delay
        pylibsythe.key_up(0x73)  # release F4
        sleep(random.randint(1573, 1995))  # random values for delay
        utils.utils.click_random_square_point(560, 410, 38, 38, 1)  # click
        sleep(random.randint(1730, 3350))  # random values for delay
        pylibsythe.key_down(0x1B)  # exit interface with ESC
        sleep(random.randint(413, 715))  # random values for delay
        pylibsythe.key_down(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(91, 119))  # random values for delay
        pylibsythe.key_up(0x7A)  # back to inventory - must be set to F11
        sleep(random.randint(87, 177))  # random values for delay


def combat_antiban():
    scrape()
    if utils.get_health(utils.FONTS.font3) < TELEPORT_THRESHOLD:  # teleports to safety and ends if you run out of food
        pylibsythe.key_down(0x75)  # clicks on spellbook
        utils.click_random_circle_point(596, 263, 1, 8)  # clicks on varrock teleport
        sleep(random.randint(556, 768))
        pylibsythe.key_down(0x74)  # press logout menu
        sleep(random.randint(310, 875))  # random values for delay
        pylibsythe.key_up(0x74)  # lift logout menu
        sleep(random.randint(10170, 13578))  # sleep for 10-13 seconds approx after combat to logout
        utils.utils.click_random_square_point(580, 415, 165, 30, 1)  # click logout
        exit()

    if random.random() < 0.031:  # chance of proc
        print("COMBAT ANTIBAN")
        pylibsythe.key_down(0x25)  # press left arrow key down for antiban
        sleep(random.randint(200, 4875))  # random values for delay
        pylibsythe.key_up(0x25)  # lift left arrow key down for antiban

    if random.random() < 0.039:  # chance of proc
        print("COMBAT ANTIBAN")
        pylibsythe.key_down(0x27)  # press right arrow key down for antiban
        sleep(random.randint(220, 2576))  # random values for delay
        pylibsythe.key_up(0x27)  # lift right arrow key up for antiban

    if random.random() < 0.013:  # chance of proc
        print("COMBAT ANTIBAN")
        pylibsythe.key_down(0x26)  # press up arrow key down for antiban
        sleep(random.randint(150, 3009))  # random values for delay
        pylibsythe.key_up(0x26)  # lift up arrow key up for antiban

    if random.random() < 0.032:  # chance of proc
        print("COMBAT ANTIBAN")
        pylibsythe.key_down(0x28)  # press down arrow key down for antiban
        sleep(random.randint(100, 8653))  # random values for delay
        pylibsythe.key_up(0x28)  # lift down arrow key up for antiban

    if random.random() < 0.017:  # down and right arrows at the same time
        print("COMBAT ANTIBAN")
        pylibsythe.key_down(0x28)  # press down arrow key down for antiban
        pylibsythe.key_down(0x27)  # press right arrow key down for antiban
        sleep(random.randint(100, 8653))  # random values for delay
        pylibsythe.key_up(0x28)  # lift down arrow key up for antiban
        sleep(random.randint(100, 8653))  # random values for delay
        pylibsythe.key_up(0x27)  # lift right arrow key up for antiban
        sleep(random.randint(220, 2576))  # random values for delay

    if random.random() < 0.037:  # down and left arrows at the same time
        print("COMBAT ANTIBAN")
        pylibsythe.key_down(0x28)  # press down arrow key down for antiban
        pylibsythe.key_down(0x25)  # press left arrow key down for antiban
        sleep(random.randint(100, 3453))  # random values for delay
        pylibsythe.key_up(0x28)  # lift down arrow key up for antiban
        sleep(random.randint(100, 6853))  # random values for delay
        pylibsythe.key_up(0x25)  # lift left arrow key up for antiban
        sleep(random.randint(120, 1276))  # random values for delay

    if random.random() < 0.027:  # up and right arrows at the same time
        print("COMBAT ANTIBAN")
        pylibsythe.key_down(0x26)  # press up arrow key down for antiban
        pylibsythe.key_down(0x27)  # press right arrow key down for antiban
        sleep(random.randint(100, 2253))  # random values for delay
        pylibsythe.key_up(0x26)  # lift up arrow key up for antiban
        sleep(random.randint(67, 3351))  # random values for delay
        pylibsythe.key_up(0x27)  # lift right arrow key up for antiban
        sleep(random.randint(287, 2176))  # random values for delay

    if random.random() < 0.015:  # up and left arrows at the same time
        print("COMBAT ANTIBAN")
        pylibsythe.key_down(0x26)  # press up arrow key down for antiban
        pylibsythe.key_down(0x25)  # press left arrow key down for antiban
        sleep(random.randint(108, 2953))  # random values for delay
        pylibsythe.key_up(0x26)  # lift up arrow key up for antiban
        sleep(random.randint(100, 4553))  # random values for delay
        pylibsythe.key_up(0x25)  # lift left arrow key up for antiban
        sleep(random.randint(127, 276))  # random values for delay


def main():
    while True:

        scrape()
        if utils.get_health(utils.FONTS.font3) < THRESHOLD:  # eats a shark when under the threshold value
            utils.click_random_bitmap_point(utils.ITEMS.shark())
        scrape()
        if utils.get_health(
                utils.FONTS.font3) < TELEPORT_THRESHOLD:  # teleports to safety and ends if you run out of food
            pylibsythe.key_down(0x75)  # clicks on spellbook
            utils.click_random_circle_point(596, 263, 1, 8)  # clicks on varrock teleport
            sleep(random.randint(556, 768))
            pylibsythe.key_down(0x74)  # press logout menu
            sleep(random.randint(310, 875))  # random values for delay
            pylibsythe.key_up(0x74)  # lift logout menu
            sleep(random.randint(10170, 13578))  # sleep for 10-13 seconds approx after combat to logout
            utils.utils.click_random_square_point(580, 415, 165, 30, 1)  # click logout
            exit()

        scrape()
        try:
            if not find_color(combat_color, *combat_area):  # if can't find green color, we're not in combat
                if npc := get_poly_point(npc_color):

                    utils.custom_mouse.random_move_mouse(npc.x, npc.y)
                    sleep(random.randint(33, 67))
                    print("Commencing extermination!!! ARGH!!!")
                    sleep(random.randint(29, 137))  # random values for delay
                    utils.click_random_circle_point(npc.x, npc.y, 1, 5)
                    sleep(random.randint(549, 979))  # random values for delay
                    combat_antiban()  # antiban during combat
                    sleep(random.randint(5576, 11645))  # wait for combat to end - change this depending on your level
        except:
            print("Couldn't find an enemy")
            list_of_antiban()
            sleep(random.randint(10325, 20763))

        if random.random() < 0.027:
            sleep(random.randint(96, 177))  # random values for delay
            utils.click_random_circle_point(npc.x, npc.y, 1, 9)  # chance to reclick
            sleep(random.randint(3039, 5137))  # waiting to get into combat

        # begin NPC related antiban
        if random.random() < 0.006:  # further mouse hovering for antiban
            utils.random_move_mouse(npc.x, npc.y)
            sleep(random.randint(33, 97))
        if random.random() < 0.007:  # further mouse hovering for antiban
            utils.random_move_mouse(npc.x, npc.y)
            sleep(random.randint(33, 137))
            utils.random_move_mouse(npc.x, npc.y)
            sleep(random.randint(67, 157))
        if random.random() < 0.009:  # further mouse hovering for antiban
            utils.random_move_mouse(npc.x, npc.y)
            sleep(random.randint(33, 137))
            utils.random_move_mouse(npc.x, npc.y)
            sleep(random.randint(67, 157))
            utils.click_random_circle_point(650, 300, 2, 50)  # right click
            sleep(random.randint(57, 357))
        if random.random() < 0.003:  # further mouse hovering for antiban
            utils.random_move_mouse(npc.x, npc.y)
            sleep(random.randint(53, 197))
            utils.random_move_mouse(npc.x, npc.y)
            sleep(random.randint(93, 147))
            utils.click_random_circle_point(650, 300, 1, 37)  # left click
            sleep(random.randint(77, 357))

        if random.random() < 0.0017:  # spin right and click npc
            print("spinning and clicking - woah!")
            pylibsythe.key_down(0x27)  # press right arrow key down for antiban
            sleep(random.randint(33, 65))  # random values for delay
            utils.click_random_circle_point(npc.x, npc.y, 1, 5)
            sleep(random.randint(189, 376))  # random values for delay
            pylibsythe.key_up(0x27)  # lift right arrow key up for antiban

        if random.random() < 0.0017:  # spin left and click npc
            print("spinning and clicking - woah!")
            pylibsythe.key_down(0x25)  # press left arrow key down for antiban
            sleep(random.randint(33, 65))  # random values for delay
            utils.click_random_circle_point(npc.x, npc.y, 1, 5)
            sleep(random.randint(148, 1176))  # random values for delay
            pylibsythe.key_up(0x25)  # lift left arrow key up for antiban

        if random.random() < 0.0017:  # spin down and click npc
            print("spinning and clicking - woah!")
            pylibsythe.key_down(0x28)  # press down arrow key down for antiban
            sleep(random.randint(33, 65))  # random values for delay
            utils.click_random_circle_point(npc.x, npc.y, 1, 5)
            sleep(random.randint(81, 564))  # random values for delay
            pylibsythe.key_up(0x28)  # lift down arrow key up for antiban

        if random.random() < 0.0017:  # spin up and click npc
            print("spinning and clicking - woah!")
            pylibsythe.key_down(0x26)  # press up arrow key down for antiban
            utils.click_random_circle_point(npc.x, npc.y, 1, 5)
            sleep(random.randint(120, 906))  # random values for delay
            pylibsythe.key_up(0x26)  # lift up arrow key up for antiban

        # mouse jitter
        if random.random() < 0.003:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 86)
            sleep(random.randint(41, 188))
        if random.random() < 0.0078:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 26)
            sleep(random.randint(41, 98))
        if random.random() < 0.0036:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 59)
            sleep(random.randint(41, 168))
        if random.random() < 0.0033:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 56)
            sleep(random.randint(47, 453))
        if random.random() < 0.0018:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 93)
            sleep(random.randint(471, 828))
        if random.random() < 0.0048:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 56)
            sleep(random.randint(481, 818))
        if random.random() < 0.00987:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 53)
            sleep(random.randint(451, 889))
        if random.random() < 0.0068:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 56)
            sleep(random.randint(343, 718))
        if random.random() < 0.00186:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 36)
            sleep(random.randint(41, 189))
        if random.random() < 0.0098:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 76)
            sleep(random.randint(41, 365))
        if random.random() < 0.00783:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 16)
            sleep(random.randint(419, 887))
        if random.random() < 0.00728:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 36)
            sleep(random.randint(341, 718))
        if random.random() < 0.00128:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 76)
            sleep(random.randint(6441, 9168))
        if random.random() < 0.00938:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 92)
            sleep(random.randint(341, 9388))
        if random.random() < 0.00348:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 26)
            sleep(random.randint(641, 728))
        if random.random() < 0.00128:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 46)
            sleep(random.randint(141, 328))
        if random.random() < 0.00638:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 36)
            sleep(random.randint(241, 618))
        if random.random() < 0.00128:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 17)
            sleep(random.randint(341, 798))
        if random.random() < 0.00128:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 49)
            sleep(random.randint(811, 982))
        if random.random() < 0.00718:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 22)
            sleep(random.randint(131, 711))
        if random.random() < 0.001238:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 32)
            sleep(random.randint(165, 199))
        if random.random() < 0.00128:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 6)
            sleep(random.randint(6433, 8632))
        if random.random() < 0.00728:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 3)
            sleep(random.randint(134, 678))
        if random.random() < 0.00128:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 16)
            sleep(random.randint(7335, 9356))
        if random.random() < 0.0088:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 36)
            sleep(random.randint(62, 168))
        if random.random() < 0.00178:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 57)
            sleep(random.randint(441, 745))
        if random.random() < 0.00928:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 61)
            sleep(random.randint(171, 888))
        if random.random() < 0.009258:
            print("Mouse to random spot")
            utils.click_random_circle_point(npc.x, npc.y, 0, 96)
            sleep(random.randint(141, 5632))

        if random.random() < 0.27:
            list_of_antiban()


main()
