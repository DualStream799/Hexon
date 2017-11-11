# -*- coding: utf-8 -*-
"""
Project: Hexon
Created on Tue Oct 24 16:4:15 2017
Current Version: 1.0.0
@author: dualstream799

"""

# ------------------------------------ LIBRARIES ------------------------------------------------ #

# Used:
import pygame
# import time

# Unused:
# import requests
# import math
# import json

# --------------------------------- INICIALIZATION ---------------------------------------------- #

# Loading PyGame:
pygame.init()
# Loading PyGame Text Font:
pygame.font.init()
# Loading Display:
display_width = 800
display_height = 450
screen = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption('Hexon v1.0', 'hex_logo_small.png')
# Loading Dsplay Updater:
clock = pygame.time.Clock()
# Loading Mouse Position:
mouse_pos = pygame

# ------------------------------------ IMAGES ------------------------------------------------- #

# Home Page Background:
# home_page_original = pygame.image.load(r'.\Images\Background\home_original.png')
home_page_purple = pygame.image.load(r'.\Images\Background\home_purple_small.png')
# home_page_green = pygame.image.load(r'.\Images\Background\home_green.png')
# home_page_blue = pygame.image.load(r'.\Images\Background\home_blue.png')
# home_page_pink = pygame.image.load(r'.\Images\Background\home_pink.png')
# home_page_orange = pygame.image.load(r'.\Images\Background\home_orange.png')
# home_page_gray = pygame.image.load(r'.\Images\Background\home_gray.png')

# Left Page Background:
# left_page_original = pygame.image.load(r'.\Images\Background\left_page_original.png')
# left_page_purple = pygame.image.load(r'.\Images\Background\home_purple_small.png")
# left_page_green = pygame.image.load(r'.\Images\Background\home_green.png')
# left_page_blue = pygame.image.load(r'.\Images\Background\home_blue.png')
# left_page_pink = pygame.image.load(r'.\Images\Background\home_pink.png')
# left_page_orange = pygame.image.load(r'.\Images\Background\home_orange.png')
# left_page_gray = pygame.image.load(r'.\Images\Background\home_gray.png')

# Right Page Background:
right_page_original = pygame.image.load(r'.\Images\Background\right_page_original_small.png')
right_glass_original = pygame.image.load(r'.\Images\Background\right_glass_original_small.png')
# right_page_purple = pygame.image.load(r'.\Images\Background\home_purple_small.png')
# right_page_green = pygame.image.load(r'.\Images\Background\home_green.png')
# right_page_blue = pygame.image.load(r'.\Images\Background\home_blue.png')
# right_page_pink = pygame.image.load(r'.\Images\Background\home_pink.png')
# right_page_orange = pygame.image.load(r'.\Images\Background\home_orange.png')
# right_page_gray = pygame.image.load(r'.\Images\Background\home_gray.png')

# Loading Page Background:


# Navigation Bar:
navbar_original = pygame.image.load(r'.\Images\Background\navbar_original.png')

# Buttons:
but_pressed = pygame.image.load(r'.\Images\Buttons\hex_but_press.png')
# but_back_left = pygame.image.load(r'.\Images\Buttons\hex_but_back_left.png')
but_back_right = pygame.image.load(r'.\Images\Buttons\hex_but_back_right.png')
but_close = pygame.image.load(r'.\Images\Buttons\hex_but_close.png')
but_menu = pygame.image.load(r'.\Images\Buttons\hex_but_menu.png')
but_play = pygame.image.load(r'.\Images\Buttons\hex_but_play.png')
but_reload = pygame.image.load(r'.\Images\Buttons\hex_but_reload.png')
but_volon = pygame.image.load(r'.\Images\Buttons\Small\hex_but_volon_small.png')
but_voloff = pygame.image.load(r'.\Images\Buttons\Small\hex_but_voloff_small.png')
but_list = pygame.image.load(r'.\Images\Buttons\hex_but_list.png')
# but_profile = pygame.image.load(r'.\Images\Buttons\hex_but_profile.png')
# but_config = pygame.image.load(r'.\Images\Buttons\hex_but_config.png')
# but_locked = pygame.image.load(r'.\Images\Buttons\hex_but_locked.png')

# Cursor:
cursor_up_center = pygame.image.load(r'.\Images\Cursor\cursor_original.png')
cursor_up_right = pygame.transform.rotate(cursor_up_center, 60)
cursor_up_left = pygame.transform.rotate(cursor_up_center, -60)
cursor_down_center = pygame.transform.rotate(cursor_up_center, 180)
cursor_down_right = pygame.transform.rotate(cursor_up_center, 120)
cursor_down_left = pygame.transform.rotate(cursor_up_center, -120)

# Itens Positions:
but_play_pos = [[(display_height - 165)/2, (display_width - 180)/2],
                [(display_height + 165)/2, (display_width + 180)/2]]
but_reload_pos = [[],
                  []]
but_volon_pos = [[92, 35],
                 [92 + 131, 214 + 142]]
but_voloff_pos = [[227, 214],
                  [227 + 125, 214 + 142]]

# ------------------------------- OBJECTS CLASSES --------------------------------------------- #

# Main element on game (User controled):
class HexCursor:
    # Loading all pre set configurations:
    position_list = ["UC", "UR", "DR", "DC", "DL", "UL"]
    index = 0
    position = position_list[index]

    def __init__(self, position):
        print(position)
        """
        if position == "UC":
            self.cursor = self.cursor_up_center
        if position == "UR":
            self.cursor = self.cursor_up_right
        if position == "UL":
            self.cursor = self.cursor_up_left
        if position == "DC":
            self.cursor = self.cursor_down_center
        if position == "DR":
            self.cursor = self.cursor_down_right
        if position == "DL":
            self.cursor = self.cursor_down_left
        self.moves = 0
        """
    # Cursor movimentation:
    """
    def move(self, moving, index):
        if self.moving == "Rotate Left":
            index -= 1
        if self.moving == "Rotate Right":
            index += 1
    """

# ------------------------------ PLAYERS CLASSES ---------------------------------------------- #

class PlayerOne:
    pass


class PlayerTwo:
    pass

# ------------------------------- MENUS FUNCTIONS ---------------------------------------------- #

def HomePage():
    # Loading Home Page (showing all the elements which compose the menu):
    screen.blit(home_page_purple, (0, 0))
    # screen.blit(but_close, (0, 0))
    screen.blit(but_play, (but_play_pos[0][0], but_play_pos[0][1]))

    screen.blit(but_volon, (but_volon_pos[0][0], but_volon_pos[0][1]))
    screen.blit(but_voloff, (227, 214))
  
    # screen.blit(but_profile, (0, 0))
    # screen.blit(but_config, (0,360))
    # screen.blit(but_close, ((display_height-165)/2, (display_width-180)/2))

    # Screen Commands:
    for event in pygame.event.get():
        # Quit Command (Calls 'GameEnd' function):
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            GameEnd()
        # Mouse Click Detection (and cosequential actions, depending where/what is clicked):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse Position(axis x and -y coordinates):
            mouse_pos_x, mouse_pos_y = event.pos
            # PLAY BUTTON Clicked:
            if (mouse_pos_x > but_play_pos[0][0] and mouse_pos_x < but_play_pos[1][0]) and (mouse_pos_y > but_play_pos[0][1] and mouse_pos_y < but_play_pos[1][1]):
                # GamePage()
                print('clicked on play')

def LeftPage():
    # Loading Left Page (showing all the elements which compose the menu):
    screen.blit(left_page_original, (0, 0))
    # screen.blit(but_close, (0, 0))
    #screen.blit(but_play, ((display_height-165)/2, (display_width-180)/2))
    # Screen Commands:
    for event in pygame.event.get():
        # Quit Command:
        if event.type == pygame.QUIT:
            GameEnd()
        # Mouse Click Detection (and cosequential actions, depending where/what is clicked):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            mouse_pos_x, mouse_pos_y = event.pos
            #  ......... BUTTON Clicked:
            if (mouse_pos_x > but_play_pos[0][0] and mouse_pos_x < but_play_pos[1][0]) and (mouse_pos_y > but_play_pos[0][1] and mouse_pos_y < but_play_pos[1][1]):
                print('clicked on ......')


def RightPage():
    # Loading Right Page (showing all the elements which compose the menu):
    screen.blit(right_page_original, (0, 0))
    screen.blit(right_glass_original, (0, 0))
    screen.blit(but_back_right, (92, -16))
    screen.blit(but_volon, (92, 214))
    screen.blit(but_voloff, (227, 214))
  
    # Screen Commands:
    for event in pygame.event.get():
        # Quit Command(created quit the 'for loop'):
        if event.type == pygame.QUIT:
            GameEnd()
            #break
        # Mouse Click Detection (and cosequential actions, depending wherbut_volone/what is clicked):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            mouse_pos_x, mouse_pos_y = event.pos
            print(mouse_pos_x, "\n", mouse_pos_y)
            #  VOLUME ON BUTTON Clicked:
            if (mouse_pos_x > but_volon_pos[0][0] and mouse_pos_x < but_play_pos[1][0]) and (mouse_pos_y > but_volon_pos[0][1] and mouse_pos_y < but_play_pos[1][1]):
                print('clicked on Vol On')
            #  VOLUME ON BUTTON Clicked:
            #if (mouse_pos_x > but_voloff_pos[0][0] and mouse_pos_x < but_play_pos[1][0]) and (mouse_pos_y > but_voloff_pos[0][1] and mouse_pos_y < but_play_pos[1][1]):
             #   print('clicked on Vol Off')
            


def GamePage():
    # screen.blit(loading_page, (0, 0))
    # time.sleep(10)
    print("Youre playing...")

def GameEnd():
    # Ends PyGame
    pygame.quit()
    # Ends Console
    quit()

# -------------------------------- GENERATION ------------------------------------------------ #

runner = True

# --------------------------------- EXECUTION ------------------------------------------------ #
# Main Loop
while (runner):
    HomePage()
    # Comands for each usable button:
    """
    for event in pygame.event.get():
        # Quit Command
        if event.type == pygame.QUIT:
            runner = False
        # Rotate Left Command
    """
    pygame.display.update()
    clock.tick(60)

# -------------------------------- FINALIZATION ---------------------------------------------- #

# Ends PyGame
pygame.quit()
# Ends Console
quit()

# ----------------------------------- IDEAS ------------------------------------------------- #

"""
X Home Page
  ----Navbar
  --------Profile Button
  --------Configuration Button
  --------Username
  --------Sinc Status
  ----Play Button
  Modes
  ----Original
  ----Flawless Mode
  Store Page
  ----Cursors
  ----Backgrounds
  ----Power Ups
  Profile Page
  ----XP conter
  ----High Scores
  --------List High Scores
  --------Graphic High Scores
  Configuration Page
  ----Mute/Sound
"""
