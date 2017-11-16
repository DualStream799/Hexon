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
import time
# Unused:
import random
# import requests
import math
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
"""
display_width = 0
display_height = 0
screen = pygame.display.set_mode((display_height, display_width), pygame.FULLSCREEN)
"""
pygame.display.set_caption('Hexon v1.0', 'hex_logo_small.png')
# Loading Dsplay Updater:
clock = pygame.time.Clock()

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

# Pause Page Background:
pause_page_original = pygame.image.load(r'.\Images\Background\pause_original_small.png')
# pause_page_purple = pygame.image.load(r'.\Images\Background\home_purple_small.png')
# pause_page_green = pygame.image.load(r'.\Images\Background\home_green.png')
# pause_page_blue = pygame.image.load(r'.\Images\Background\home_blue.png')
# pause_page_pink = pygame.image.load(r'.\Images\Background\home_pink.png')
# pause_page_orange = pygame.image.load(r'.\Images\Background\home_orange.png')
# pause_page_gray = pygame.image.load(r'.\Images\Background\home_gray.png')

# Game Page Background:
game_space = pygame.image.load(r'.\Images\Background\Game Screen\space_background.png')
# game_page_original = pygame.image.load(r'.\Images\Background\home_original.png')
game_page_purple = pygame.image.load(r'.\Images\Background\game_purple_small.png')
# game_page_green = pygame.image.load(r'.\Images\Background\home_green.png')
# game_page_blue = pygame.image.load(r'.\Images\Background\home_blue.png')
# game_page_pink = pygame.image.load(r'.\Images\Background\home_pink.png')
# game_page_orange = pygame.image.load(r'.\Images\Background\home_orange.png')
# game_page_gray = pygame.image.load(r'.\Images\Background\home_gray.png')
# Loading Page Background:

# Navigation Bar:
# navbar_original = pygame.image.load(r'.\Images\Background\NavBar\navbar_original.png')

# Buttons:
but_pressed = pygame.image.load(r'.\Images\Buttons\Small\hex_but_press_all.png')
but_pressed_big = pygame.image.load(r'.\Images\Buttons\Small\hex_but_press_play.png')
but_play = pygame.image.load(r'.\Images\Buttons\Small\hex_but_play.png')
but_play_base = pygame.image.load(r'.\Images\Buttons\Small\hex_but_play_base.png')

# but_back_left = pygame.image.load(r'.\Images\Buttons\hex_but_back_left.png')
but_back_right = pygame.image.load(r'.\Images\Buttons\hex_but_back_right.png')
but_close = pygame.image.load(r'.\Images\Buttons\Small\hex_but_close_small.png')
but_menu = pygame.image.load(r'.\Images\Buttons\hex_but_menu.png')
but_reload = pygame.image.load(r'.\Images\Buttons\hex_but_reload.png')
but_volon = pygame.image.load(r'.\Images\Buttons\Small\hex_but_volon_small.png')
but_voloff = pygame.image.load(r'.\Images\Buttons\Small\hex_but_voloff_small.png')
but_list = pygame.image.load(r'.\Images\Buttons\hex_but_list.png')
but_profile = pygame.image.load(r'.\Images\Buttons\Small\hex_but_profile_small.png')
# but_config = pygame.image.load(r'.\Images\Buttons\hex_but_config.png')
# but_locked = pygame.image.load(r'.\Images\Buttons\hex_but_locked.png')
but_pause = pygame.image.load(r'.\Images\Buttons\Small\hex_but_pause_small.png')
but_pause_yes = pygame.image.load(r'.\Images\Buttons\Small\hex_but_pause_yes.png')
but_pause_no = pygame.image.load(r'.\Images\Buttons\Small\hex_but_pause_no.png')
but_star = pygame.image.load(r'.\Images\Buttons\Small\hex_but_star.png')
# Cursor:
cursor_up_center = pygame.image.load(r'.\Images\Cursor\cursor_original.png')
cursor_up_right = pygame.transform.rotate(cursor_up_center, 60)
cursor_up_left = pygame.transform.rotate(cursor_up_center, -60)
cursor_down_center = pygame.transform.rotate(cursor_up_center, 180)
cursor_down_right = pygame.transform.rotate(cursor_up_center, 120)
cursor_down_left = pygame.transform.rotate(cursor_up_center, -120)

# Colliders:

# Planets:
planet_original = pygame.image.load(r'.\Images\Objects\Planets\planet_original.png')

# ----------------------------------- POSITIONS ------------------------------------------------ #

# Buttons:
but_play_pos = [[int((display_height - 180)/2), int((display_width - 180)/2)], [int((display_height + 165)/2), int((display_width + 180)/2)]]
but_close_pos = [[169, 146], [169 + 109, 146 + 120]]
but_volon_pos = [[338, 243], [338 + 106, 243 + 122]]
but_voloff_pos = [[338, 243], [338 + 106, 243 + 122]]
but_profile_pos = [[2, 243], [2 + 109, 243 + 120]]
but_pause_pos = [[375, 3], [375 + 73, 3 + 81]]
but_pause_yes_pos = [[55, 347], [55 + 81, 347 + 92]]
but_pause_no_pos = [[333, 347], [333 + 81, 347 + 93]]
but_star_pos = [[337, 438], [337 + 110, 438 + 121]]
"""
but_config_pos = [[2, 243], [2 + 109, 243 + 120]]
but_contact_pos = [[2, 243], [2 + 109, 243 + 120]]
"""

# Planets:
planet_pos = [[int((display_height - 121)/2), int((display_width - 121)/2)], [int((display_height + 121)/2), int((display_width + 121)/2)]]

# -------------------------------- ROTATION SPEED ------------------------------------------------ #

planet_speed = 1

# ------------------------------- OBJECTS CLASSES --------------------------------------------- #

# Main element on game (User controled):
def HexCursor():
	# Loading all pre set configurations:
	position_list = ["UC", "UR", "DR", "DC", "DL", "UL"]
	index = 0
	position = position_list[index]
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
# ------------------------------ OBJECTS CLASSES ---------------------------------------------- #

# Collider Class (Objects which must be reflected):
class Collider:
	def __init__(self):
		self.speed



# Barrier Class (Object User controled):
class Barrier:
	def __init__(self, sprite):
		self.speed_x = speed_x
		self.speed_y = speed_y
		self.sprite = sprite
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		screen.blit(pos_x, pos_y)
	# Clockwise Rotation function:
	def rotate_CL(self):
		pos_x = self.radius*math.sin(pos_x)
		pos_y = self.radius*math.cos(pos_y)
	# Anticlockwise Rotation function:
	def rotate_ACL(self):
		pos_x = self.radius*math.sin(-pos_x)
		pos_y = self.radius*math.sin(-pos_y)

# ------------------------------ PLAYERS CLASSES ---------------------------------------------- #

class PlayerOne:
	pass


class PlayerTwo:
	pass

# ----------------------------- SECONDARY FUNCTIONS -------------------------------------------- #

# Rotate image in fixed center
def image_rotation_centered(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


# ------------------------------- MENUS FUNCTIONS ---------------------------------------------- #
# Main loop
def HomePage():
	# Loading all pre set configurations:
	Volume_on = True
	# Loop Controler:
	home_runner = True
	# Main Loop:
	while home_runner:	
		# Loading Home Page (showing all the elements which compose the menu):
		screen.blit(home_page_purple, (0, 0))
		screen.blit(but_close, (but_close_pos[0][0], but_close_pos[0][1]))
		screen.blit(but_volon, (but_volon_pos[0][0], but_volon_pos[0][1]))
		screen.blit(but_profile, (but_profile_pos[0][0], but_profile_pos[0][1]))
		screen.blit(but_star, (but_star_pos[0][0], but_star_pos[0][1]))
		screen.blit(but_play, (but_play_pos[0][0], but_play_pos[0][1]))

		# screen.blit(but_config, (but_config_pos[0][0], but_config_pos[0][1]))
		# screen.blit(but_contact, (but_contact_pos[0][0], but_contact_pos[0][1]))
		# Screen Commands:
		for event in pygame.event.get():
			# Quit Command (Calls 'GameEnd' function):
			if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
				GameEnd()
			# Mouse Click Detection (and cosequential actions, depending where/what is clicked):
			if event.type == pygame.MOUSEBUTTONDOWN:
				# Mouse Position (axis x and -y coordinates):
				mouse_pos_x, mouse_pos_y = event.pos
				# Mouse Tracking:
				print(mouse_pos_x, mouse_pos_y)

				# CLOSE BUTTON Clicked:
				if (mouse_pos_x in range(but_close_pos[0][0], but_close_pos[1][0])) and (mouse_pos_y in range(but_close_pos[0][1], but_close_pos[1][1])):
					screen.blit(but_pressed, (but_close_pos[0][0], but_close_pos[0][1]))
					print("Close Clicked")
					GameEnd()

				# PLAY BUTTON Clicked:
				if (mouse_pos_x in  range(but_play_pos[0][0], but_play_pos[1][0])) and (mouse_pos_y in range(but_play_pos[0][1], but_play_pos[1][1])):
					screen.blit(but_pressed_big, (but_play_pos[0][0], but_play_pos[0][1]))
					print('Play Clicked')
					GamePage()

				# VOLUME ON BUTTON Clicked:
				if (mouse_pos_x in range(but_volon_pos[0][0], but_volon_pos[1][0])) and (mouse_pos_y in range(but_volon_pos[0][1], but_volon_pos[1][1])) and Volume_on == True:
					screen.blit(but_pressed, (but_volon_pos[0][0], but_volon_pos[0][1]))
					screen.blit(but_voloff, (but_voloff_pos[0][0], but_voloff_pos[0][1]))
					Volume_on = False
					print("VolOn Clicked")

				# VOLUME OFF BUTTON Clicked:
				if (mouse_pos_x in range(but_voloff_pos[0][0], but_voloff_pos[1][0])) and (mouse_pos_y in range(but_voloff_pos[0][1], but_voloff_pos[1][1])) and Volume_on == False:
					screen.blit(but_pressed, (but_voloff_pos[0][0], but_voloff_pos[0][1]))
					screen.blit(but_volon, (but_voloff_pos[0][0], but_voloff_pos[0][1]))
					Volume_on = True
					print("VolOff Clicked")
		
				# PROFILE BUTTON Clicked:
				if (mouse_pos_x in range(but_profile_pos[0][0], but_profile_pos[1][0])) and (mouse_pos_y in range(but_profile_pos[0][1], but_profile_pos[1][1])):
					screen.blit(but_pressed, (but_profile_pos[0][0], but_profile_pos[0][1]))
					print("Profile Clicked")

		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)


def PausePage():
	# Loop Controler:
	pause_runner = True
	# Pause Loop:
	while pause_runner:
		# Loading Home Page (showing all the elements which compose the menu):
		screen.blit(game_space, (0, 0))
		screen.blit(pause_page_original, (0, 0))
		screen.blit(but_pause_yes, (but_pause_yes_pos[0][0], but_pause_yes_pos[0][1]))
		screen.blit(but_pause_no, (but_pause_no_pos[0][0], but_pause_no_pos[0][1]))
		# Screen commands:
		for event in pygame.event.get():
			# Quit Command (Calls 'GameEnd' function): 
			if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
				pause_runner = False


			if event.type == pygame.MOUSEBUTTONDOWN:
				# Mouse Position (axis x and -y coordinates):
				mouse_pos_x, mouse_pos_y = event.pos
				# Mouse Tracking:
				print(mouse_pos_x, mouse_pos_y)

				# YES BUTTON Clicked:
				if (mouse_pos_x in range(but_pause_yes_pos[0][0], but_pause_yes_pos[1][0])) and (mouse_pos_y in range(but_pause_yes_pos[0][1], but_pause_yes_pos[1][1])):
					print("Pause Yes Clicked")
					pause_runner = False

				# NO BUTTON Clicked:
				if (mouse_pos_x in range(but_pause_no_pos[0][0], but_pause_no_pos[1][0])) and (mouse_pos_y in range(but_pause_no_pos[0][1], but_pause_no_pos[1][1])):
					print("Pause No Clicked")
					pause_runner = False
					game_runner = False
		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)

def ProfilePage():
	pass


def LoadingPage():
	pass  


def GamePage():
	# Loop Controler:
	game_runner = True
	planet_angle = 0
	# Game Loop
	while game_runner:
		# Loading Home Page (showing all the elements which compose the menu):
		rotating_planet = image_rotation_centered(planet_original, planet_angle)
		screen.blit(game_space, (0, 0))
		screen.blit(but_pause, (but_pause_pos[0][0], but_pause_pos[0][1])) 
		screen.blit(planet_original, (planet_pos[0][0], planet_pos[0][1]))
		screen.blit(rotating_planet, (planet_pos[0][0], planet_pos[0][1]))
		# screen.blit(loading_page, (0, 0))
		# time.sleep(10)
		# Screen Commands:
		for event in pygame.event.get():
			# Quit Command (Calls 'GameEnd' function): 
			if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
				game_runner = False
			# Pause Command (Calls 'PauseMode' function): 
			if event.type == pygame.K_SPACE:
				PausePage()
				
			# CLOCKWISE BARRIER Command (Make Barrier rotate to the right):
			if event.type == pygame.K_a:
				pass
			# Clockwise Barrier Command (Make Barrier rotate to the left):
			if event.type == pygame.K_d:
				pass
			# Mouse Click Detection (and cosequential actions, depending where/what is clicked):
			if event.type == pygame.MOUSEBUTTONDOWN:
				# Mouse Position(axis x and -y coordinates):
				mouse_pos_x, mouse_pos_y = event.pos
				# Mouse Tracking:
				print(mouse_pos_x, mouse_pos_y)

				# PAUSE BUTTON Clicked:
				if (mouse_pos_x in range(but_pause_pos[0][0], but_pause_pos[1][0])) and (mouse_pos_y in range(but_pause_pos[0][1], but_pause_pos[1][1])):
					screen.blit(but_pressed, (but_pause_pos[0][0], but_pause_pos[0][1]))
					print("Pause Clicked")
					PausePage()
		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)
		if planet_angle >= 360:
			planet_angle = 0
		else:
			planet_angle += 0.5


def GameEnd():
	# Ends PyGame
	pygame.quit()
	# Ends Console
	quit()

# -------------------------------- GENERATION ------------------------------------------------ #


# --------------------------------- EXECUTION ------------------------------------------------ #

HomePage()

# -------------------------------- FINALIZATION ---------------------------------------------- #

# Ends PyGame
pygame.quit()
# Ends Console
quit()

# ----------------------------------- IDEAS ------------------------------------------------- #

"""
X Home Page
----Navbar

----Contact Button
--------
--------
--------
----PauseMenu
----Configuration Button
--------Username
--------Sinc Status
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
"""
