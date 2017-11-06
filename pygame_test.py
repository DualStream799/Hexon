# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:4:15 2017

@author: dualstream799
"""

# Importing libraries:
import pygame
import time
import requests
import math
import json

# --------------------------------- INICIALIZATION -------------------------------- #
# Loading PyGame:
pygame.init()
# Loading PyGame Text Font:
pygame.font.init()
# Loading Display:
display_width = 600
display_height = 720
pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption("Hexon", "")
pygame.time.Clock()


basic_font = pygame.font.SysFont("Magneto", 30, True)

# ------------------------------------ IMAGES ------------------------------------- #
# Background:
#home_original = pygame.image.load(r".\Images\Background\home_original.png")
home_purple = pygame.image.load(r".\Images\Background\home_purple.png")
#home_green = pygame.image.load(r".\Images\Background\home_green.png")
#home_blue = pygame.image.load(r".\Images\Background\home_blue.png")
#home_pink = pygame.image.load(r".\Images\Background\home_pink.png")
#home_orange = pygame.image.load(r".\Images\Background\home_orange.png")
#home_gray = pygame.image.load(r".\Images\Background\home_gray.png")

# Buttons:
but_pressed = pygame.image.load(r".\Images\Buttons\hex_but_press.png")
#but_back_left = pygame.image.load(r".\Images\Buttons\hex_but_back_left.png")
but_back_right = pygame.image.load(r".\Images\Buttons\hex_but_back_right.png")
but_close = pygame.image.load(r".\Images\Buttons\hex_but_close.png")
but_menu = pygame.image.load(r".\Images\Buttons\hex_but_menu.png")
but_play = pygame.image.load(r".\Images\Buttons\hex_but_play.png")
but_reload = pygame.image.load(r".\Images\Buttons\hex_but_reload.png")
but_volon = pygame.image.load(r".\Images\Buttons\hex_but_volon.png")
but_voloff = pygame.image.load(r".\Images\Buttons\hex_but_voloff.png")
but_list = pygame.image.load(r".\Images\Buttons\hex_but_list.png")


# ------------------------------- OBJECTS CLASSES --------------------------------- #
# Main element on game (User controled):
class HexCursor:
	# Loading all pre set configurations:
	def __init__(self, image):
		self.cursor_up_center = pygame.image.load(r".\Images\Cursor\cursor_original.png")
		self.cursor_up_right = pygame.transform.rotate(self.cursor_up_center, 60)
		self.cursor_up_left = pygame.transform.rotate(self.cursor_up_center, -60)
		self.cursor_down_center = pygame.transform.rotate(self.cursor_up_center, 180)
		self.cursor_down_right = pygame.transform.rotate(self.cursor_up_center, 120)
		self.cursor_down_left = pygame.transform.rotate(self.cursor_up_center, -120)
		if position == "UC":
			self.cursor = self.cursor_up_center
		if position == "UR":
			self.cursor = self.cursor_up_center
		if position == "UL":
			self.cursor = self.cursor_up_center
		if position == "DC":
			self.cursor = self.cursor_up_center
		if position == "DR":
			self.cursor = self.cursor_up_center
		if position == "DL":
			self.cursor = self.cursor_up_center
		self.moves = 0
		position_list = ["UC", "UR", "DR", "DC", "DL", "UL"]
		index = 0
		position = position_list[index]
	# Cursor movimentation:
	def move(self):
		if self.moving == "Rotate Left":
			index -= 1
		if self.moving == "Rotate Right":
			index += 1
# Testing Window
i = 0
while i < 3:
    i += 1
    time.sleep(1)
# -------------------------------- FINALIZATION ----------------------------------- #
# Ends PyGame
pygame.quit()
# Ends Console
quit()

# ----------------------------------- IDEAS -------------------------------------- #
"""
Home Page
	NavBar
		Profile Button
		Configuration Button
		Username
		Sinc Status
	Play Button
Modes
	Original
	Flawless Mode
Store Page
	Cursors
	Backgrounds
	Power Ups
Profile Page
	XP conter
	High Scores
		List High Scores
		Graphic High Scores
Configuration Page
	Mute/Sound
"""
