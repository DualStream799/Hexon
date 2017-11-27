# -*- coding: utf-8 -*-
"""
Project: Hexon
Created on Tue Oct 24 16:4:15 2017
Current Version: 1.0.0
@author: dualstream799

"""

# ------------------------------------ LIBRARIES ------------------------------------------------ #

# Used:
from scipy.integrate import odeint 
from math import pi
import numpy as np
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
pygame.display.set_caption('Hexon v1.0', '.\hex_logo_small.png')
# Loading Dsplay Updater:
clock = pygame.time.Clock()

# ------------------------------------ IMAGES ------------------------------------------------- #

# Cursor:

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
but_config = pygame.image.load(r'.\Images\Buttons\Small\hex_but_config_small.png')
but_locked = pygame.image.load(r'.\Images\Buttons\Small\hex_but_locked_small.png')
but_pause = pygame.image.load(r'.\Images\Buttons\Small\hex_but_pause_small.png')
but_pause_yes = pygame.image.load(r'.\Images\Buttons\Small\hex_but_pause_yes.png')
but_pause_no = pygame.image.load(r'.\Images\Buttons\Small\hex_but_pause_no.png')
but_star = pygame.image.load(r'.\Images\Buttons\Small\hex_but_star.png')
but_store = pygame.image.load(r'.\Images\Buttons\Small\hex_but_store_small.png')
but_logoff = pygame.image.load(r'.\Images\Buttons\Small\hex_but_logoff_small.png')
#but_player1 = pygame.image.load(r'.\Images\Buttons\Small\hex_but_profile_small.png')
#but_player2 = pygame.image.load(r'.\Images\Buttons\Small\hex_but_profile_small.png')

# Barrier:
cursor_purple = pygame.image.load(r'.\Images\Cursor\Barrier.png')

# Colliders:
fast_comet_original = pygame.image.load(r'.\Images\Colliders\fast_comet_original.png')


# PowerUps:


# Planets:
planet_original = pygame.image.load(r'.\Images\Planets\planet_original.png')

# Spacecrafts:
ship_F5S4 = pygame.image.load(r'.\Images\Spacecrafts\Spacecraft_F5S4.png')


# --------------------------------- ROTATION SPEED --------------------------------------------- #

planet_speed = 1

# -------------------------------- OBJECTS CLASSES --------------------------------------------- #



# ------------------------------ OBJECTS CLASSES ---------------------------------------------- #


# Collider Class (Objects which must be reflected):
class Collider:
	def __init__(self):
		pass
	

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


# Control commands for Player One:
class PlayerOne:
	def __init__(self):
		pass

# Control commands for Player Two:
class PlayerTwo:
	def __init__(self):
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

# Orbit position generator (reconfigurated for pixel unit):
def orbital_trajectory(radius):
    """
    Creates couple of lists (X-axis and Y-axis position lists) 
    based on Earth translation around the Sun.

    Libraries importation required:
    - odeint ( from scipy.integrate import odeint )
    - np     ( import numpy as np )
    - pi     ( from math import pi )

    Parameters:
    - radius (int or float value)

    Returns: 
    - solution_pixels_rounded (numpy.ndarray)
    """

    # Unit converters:
    AU = 149597870700  # Astronomic Unit in m
    P = 3.156*10**7    # year in seconds
    # Initials Conditions [x0, y0, Vx0, Vy0]:
    val_init = [1, 0, 0, 29.78*10**3/AU*P]
    # Differential Equations:
    def EqDif(val_init, t):
        # Loading initial values:
        x = val_init[0]
        y = val_init[1]
        Vx = val_init[2]
        Vy = val_init[3]
        # Derivatives:
        dxdt = Vx
        dydt = Vy
        dVxdt = -4*pi**2*(x/(x**2 + y**2)**(3/2))
        dVydt = -4*pi**2*(y/(x**2 + y**2)**(3/2))
        return [dxdt, dydt, dVxdt, dVydt]
    # Time list:
    time = np.arange(0, 1, 1/360)
    # Numeric integration:
    solution = odeint(EqDif, val_init, time)
    # Converting values (in AU) for screen size proportion (pixels):
    solution_pixels = radius*solution
    # Rounding numpers for int numbers (pixels are always int values):
    solution_pixels_rounded = np.around(solution_pixels)
    # Returned data
    return solution_pixels_rounded


# Generate a ramdom position for a Collider:
def collider_spawn():
	random_x = random.randint(0, display_height)
	random_y = random.randint(0, display_width)
	collider_angle = math.arctan(random_x/random_y)
	
	return (random_x, random_y), collider_angle


# ----------------------------------- POSITIONS ------------------------------------------------ #


# Buttons:
but_play_pos = [[int((display_height - 180)/2), int((display_width - 180)/2)], [int((display_height + 165)/2), int((display_width + 180)/2)]]
but_logoff_pos = [[169, 146], [169 + 109, 146 + 120]]
but_volon_pos = [[338, 243], [338 + 106, 243 + 122]]
but_voloff_pos = [[338, 243], [338 + 106, 243 + 122]]
but_profile_pos = [[2, 243], [2 + 109, 243 + 120]]
but_pause_pos = [[375, 3], [375 + 73, 3 + 81]]
but_pause_yes_pos = [[55, 347], [55 + 81, 347 + 92]]
but_pause_no_pos = [[333, 347], [333 + 81, 347 + 93]]
but_star_pos = [[169, 535], [169  + 110, 535 + 121]]
but_config_pos = [[338, 435], [338  + 110, 435 + 121]]
but_store_pos = [[-1, 437], [-1  + 110, 437 + 121]]

# Planets:
planet_pos = [[int((display_height - 121)/2), int((display_width - 121)/2)], [int((display_height + 121)/2), int((display_width + 121)/2)]]

# Barrier X axis:
cursor_x_pos = orbital_trajectory(117)[:, 0] + int((display_height - 121)/2)

# Barrier Y axis:
cursor_y_pos = orbital_trajectory(117)[:, 1] + int((display_width - 121)/2)


# ------------------------------------- LOGIN PAGE ---------------------------------------------- #


# Main loop
def LoginPage():
	# Loading Home Page (showing all the elements which compose the menu):
	#screen.blit(home_page_purple, (0, 0))
	pass


# -------------------------------------- HOME PAGE ---------------------------------------------- #


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
		screen.blit(but_logoff, (but_logoff_pos[0][0], but_logoff_pos[0][1]))
		screen.blit(but_volon, (but_volon_pos[0][0], but_volon_pos[0][1]))
		screen.blit(but_profile, (but_profile_pos[0][0], but_profile_pos[0][1]))
		screen.blit(but_star, (but_star_pos[0][0], but_star_pos[0][1]))
		screen.blit(but_play, (but_play_pos[0][0], but_play_pos[0][1]))
		screen.blit(but_config, (but_config_pos[0][0], but_config_pos[0][1]))
		screen.blit(but_store, (but_store_pos[0][0], but_store_pos[0][1]))
		# Screen Commands:
		for event in pygame.event.get():
			# Quit Command (Calls 'GameEnd' function):
			if event.type == pygame.QUIT:
				GameEnd()
			# Keyboard Click Detection (and cosequential actions, depending where/what is clicked):
			if event.type == pygame.KEYDOWN:	
				# Exit Command (Calls 'GameEnd' function):
				if event.key == pygame.K_ESCAPE:
					GameEnd()
				# Enter Command (Calls 'GameEnd' function):
				if event.key == pygame.K_SPACE:
					GamePage()
			# Mouse Click Detection (and cosequential actions, depending where/what is clicked):
			if event.type == pygame.MOUSEBUTTONDOWN:
				# Mouse Position (axis x and -y coordinates):
				mouse_pos_x, mouse_pos_y = event.pos
				# Mouse Tracking:
				print(mouse_pos_x, mouse_pos_y)

				# CLOSE BUTTON Clicked:
				if (mouse_pos_x in range(but_logoff_pos[0][0], but_logoff_pos[1][0])) and (mouse_pos_y in range(but_logoff_pos[0][1], but_logoff_pos[1][1])):
					screen.blit(but_pressed, (but_logoff_pos[0][0], but_logoff_pos[0][1]))
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


# ------------------------------------- PAUSE PAGE ---------------------------------------------- #


def PausePage():
	# Loop Controler:
	pause_runner = True
	exit_trigger = True
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
#					exit_trigger = False
#	if exit_trigger == False:
#		return False
		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)


def ProfilePage():
	pass


def LoadingPage():
	pass  


# -------------------------------------- GAME PAGE ---------------------------------------------- #


def GamePage():
	# Loop Controler:
	game_runner = True
	# Movement Delayer (Used to delay animation movement speed avoiding user visual discomfort):
	ticker = 0
	# Rotation/Translation Controlers:
	planet_angle = 0
	barrier_angle = 0
	index_barrier_pos = 0
	barrier_runner = True
	# Game Loop
	while game_runner:
		rotating_planet = image_rotation_centered(planet_original, planet_angle)
		rotating_barrier = image_rotation_centered(cursor_purple, barrier_angle)
		# Loading Home Page (showing all the elements which compose the menu):
		screen.blit(game_space, (0, 0))
		screen.blit(but_pause, (but_pause_pos[0][0], but_pause_pos[0][1])) 
		screen.blit(planet_original, (planet_pos[0][0], planet_pos[0][1]))
		screen.blit(rotating_planet, (planet_pos[0][0], planet_pos[0][1]))
		screen.blit(rotating_barrier, (cursor_x_pos[index_barrier_pos], cursor_y_pos[index_barrier_pos]))
		# Screen Commands:
		for event in pygame.event.get():
			# Quit Command (Calls 'GameEnd' function): 
			if event.type == pygame.QUIT:
				GameEnd()
			# Keyboard Click Detection (and cosequential actions, depending where/what is clicked):
			if event.type == pygame.KEYDOWN:	
				# Exit Command (Ends 'GamePage' function and return to 'MenuPage'):
				if event.key == pygame.K_ESCAPE:
					game_runner = False
				# Pause Command (Calls 'PauseMode' function): 
				if event.key == pygame.K_SPACE:
					PausePage()	
				# CLOCKWISE Barrier Command (Make Barrier rotate to the right):
				if event.key == pygame.K_d:
					barrier_runner = False
					print(index_barrier_pos)
				# ANTICLOCKWISE Barrier Command (Make Barrier rotate to the left):
				if event.key == pygame.K_a:
					barrier_runner = True
					print(index_barrier_pos)
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

		if PausePage == False:
			game_runner = False
		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)
		# Planet Continuous Rotation (reset planet angle counter):
		if planet_angle >= 360:
			planet_angle = 0
		else:
			planet_angle += 0.5
		# Planet Continuous Translation 'n Rotation (reset barrier angle counter and alternates angle rotation and position list index):
		if barrier_angle >= 360:
			barrier_angle = 0
		elif barrier_runner == True:
			barrier_angle += 1
			index_barrier_pos -= 1
		elif barrier_runner == False:
			barrier_angle -= 1
			index_barrier_pos += 1	
		# Barrier Continuous Translation (reset index position counter):
		if index_barrier_pos < 0:
			index_barrier_pos = len(cursor_x_pos) - 1
		if index_barrier_pos > len(cursor_x_pos) - 1:
			index_barrier_pos = 0
		# Rate Command Control (check pressed buttons each 3 loop cycles):
		if ticker >= 3:
			ticker = 0
		else:
			ticker += 1


def GameEnd():
	# Ends PyGame
	pygame.quit()
	# Ends Console
	quit()

# --------------------------------- EXECUTION ------------------------------------------------ #

HomePage()

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
