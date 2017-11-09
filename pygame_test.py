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
pygame.display.set_caption("Hexon v1.0", "/hex_logo_small.png")
# Loading Dsplay Updater:
clock = pygame.time.Clock()
# Loading Mouse Position:
# mouse_pos = pygame.mouse.get_pos()

# ------------------------------------ IMAGES ------------------------------------------------- #

# Home Page Background:
# home_page_original = pygame.image.load(r".\Images\Background\home_original.png")
home_page_purple = pygame.image.load("Images/Background/home_purple_small.png").convert()
# home_page_green = pygame.image.load(r".\Images\Background\home_green.png")
# home_page_blue = pygame.image.load(r".\Images\Background\home_blue.png")
# home_page_pink = pygame.image.load(r".\Images\Background\home_pink.png")
# home_page_orange = pygame.image.load(r".\Images\Background\home_orange.png")
# home_page_gray = pygame.image.load(r".\Images\Background\home_gray.png")

# Left Page Background:
# left_page_original = pygame.image.load(r".\Images\Background\left_page_original.png")
# left_page_purple = pygame.image.load(r".\Images\Background\home_purple_small.png")
# left_page_green = pygame.image.load(r".\Images\Background\home_green.png")
# left_page_blue = pygame.image.load(r".\Images\Background\home_blue.png")
# left_page_pink = pygame.image.load(r".\Images\Background\home_pink.png")
# left_page_orange = pygame.image.load(r".\Images\Background\home_orange.png")
# left_page_gray = pygame.image.load(r".\Images\Background\home_gray.png")

# Right Page Background:
# right_page_original = pygame.image.load(r".\Images\Background\right_page_original.png")
# right_page_purple = pygame.image.load(r".\Images\Background\home_purple_small.png")
# right_page_green = pygame.image.load(r".\Images\Background\home_green.png")
# right_page_blue = pygame.image.load(r".\Images\Background\home_blue.png")
# right_page_pink = pygame.image.load(r".\Images\Background\home_pink.png")
# right_page_orange = pygame.image.load(r".\Images\Background\home_orange.png")
# right_page_gray = pygame.image.load(r".\Images\Background\home_gray.png")

# Loading Page Background:
#


# Buttons:
but_pressed = pygame.image.load('Images/Buttons/hex_but_press.png').convert()
# but_back_left = pygame.image.load(r".\Images\Buttons\hex_but_back_left.png")
but_back_right = pygame.image.load("Images/Buttons/hex_but_back_right.png").convert()
but_close = pygame.image.load("Images/Buttons/hex_but_close.png").convert()
but_menu = pygame.image.load("Images/Buttons/hex_but_menu.png").convert()
but_play = pygame.image.load("Images/Buttons/hex_but_play.png").convert()
but_reload = pygame.image.load("Images/Buttons/hex_but_reload.png").convert()
but_volon = pygame.image.load("Images/Buttons/hex_but_volon.png").convert()
but_voloff = pygame.image.load("Images/Buttons/hex_but_voloff.png").convert()
but_list = pygame.image.load("Images/Buttons/hex_but_list.png").convert()
# but_profile = pygame.image.load(r".\Images\Buttons\hex_but_profile.png")
# but_config = pygame.image.load(r".\Images\Buttons\hex_but_config.png")
# but_locked = pygame.image.load(r".\Images\Buttons\hex_but_locked.png")

# Cursor:
cursor_up_center = pygame.image.load("Images/Cursor/cursor_original.png").convert()
cursor_up_right = pygame.transform.rotate(cursor_up_center, 60)
cursor_up_left = pygame.transform.rotate(cursor_up_center, -60)
cursor_down_center = pygame.transform.rotate(cursor_up_center, 180)
cursor_down_right = pygame.transform.rotate(cursor_up_center, 120)
cursor_down_left = pygame.transform.rotate(cursor_up_center, -120)


# Positions:
but_play_pos = ((display_height-165)/2), ((display_width-180)/2) 

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


# ------------------------------- MENUS CLASSES ---------------------------------------------- #

class HomePage:
    def __init__(self):
        screen.blit(home_page_purple, (0, 0))
        screen.blit(but_play, ((display_height-165)/2, (display_width-180)/2))
        # screen.blit(but_profile, (0, 0))
        # screen.blit(but_config, (0,360))
        # screen.blit(but_close, ((display_height-165)/2, (display_width-180)/2))
        for event in pygame.event.get():
            # Quit Command:
            if event.type == pygame.QUIT:
                runner = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                # clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
            # Mouse Click Detection (and cosequential actions, depending where is clicked):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos[0], mouse_pos[1] = event.pos
                # Click on Play Button (Loads GamePage):
                if but_play.get_rect().collidepoint(mouse_pos):
                    # screen.blit(but_pressed, ((display_height-165)/2, (display_width-180)/2))
                    # game_runner = True
                    # GamePage()
                    print("Cliked is working!")


class LeftPage:

    def __init__(self):
        pass


class RightPage:

    def __init__(self):
        pass


class GamePage:

    def __init__(self):
        # screen.blit(loading_page, (0, 0))
        # time.sleep(10)
        print("Youre playing...")

# -------------------------------- GENERATION ------------------------------------------------ #

runner = True

# --------------------------------- EXECUTION ------------------------------------------------ #
# Main Loop
if runner is True:
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
# quit()

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
