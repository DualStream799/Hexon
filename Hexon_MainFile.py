# -*- coding: utf-8 -*-
"""
Project: Hexon
Created on Tue Oct 24 16:4:15 2017
Current Version: 1.0.0
@author: dualstream799

"""


# ------------------------------------ LIBRARIES ------------------------------------------------ #

# Python built in libraries:
from scipy.integrate import odeint 
from random import randint
from math import degrees
from math import atan
from math import sin
from math import cos
from math import pi
import numpy as np
import pygame
import random
import time
import math
import json
import sys
import os
# External libraries:
from textbox import TextBox
import pygame_functions as pyfunc

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


# Letters LowerCase:
# letter_a = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_a.png')
# letter_b = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_b.png')
# letter_c = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_c.png')
# letter_d = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_d.png')
# letter_e = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_e.png')
# letter_f = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_f.png')
# letter_g = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_g.png')
# letter_h = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_h.png')
# letter_i = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_i.png')
# letter_j = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_j.png')
# letter_k = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_k.png')
# letter_l = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_l.png')
# letter_m = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_m.png')
# letter_n = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_n.png')
# letter_o = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_o.png')
# letter_p = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_p.png')
# letter_q = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_q.png')
# letter_r = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_r.png')
# letter_s = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_s.png')
# letter_t = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_t.png')
# letter_u = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_u.png')
# letter_v = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_v.png')
# letter_w = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_w.png')
# letter_x = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_x.png')
# letter_y = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_y.png')
# letter_z = pygame.image.load(r'.\Images\Alphabet\Lowercase\letter_z.png')

# Letters Capital:
letter_A = pygame.image.load(r'.\Images\Alphabet\Capital\letter_A.png')
letter_B = pygame.image.load(r'.\Images\Alphabet\Capital\letter_B.png')
letter_C = pygame.image.load(r'.\Images\Alphabet\Capital\letter_C.png')
letter_D = pygame.image.load(r'.\Images\Alphabet\Capital\letter_D.png')
letter_E = pygame.image.load(r'.\Images\Alphabet\Capital\letter_E.png')
letter_F = pygame.image.load(r'.\Images\Alphabet\Capital\letter_F.png')
letter_G = pygame.image.load(r'.\Images\Alphabet\Capital\letter_G.png')
letter_H = pygame.image.load(r'.\Images\Alphabet\Capital\letter_H.png')
letter_I = pygame.image.load(r'.\Images\Alphabet\Capital\letter_I.png')
letter_J = pygame.image.load(r'.\Images\Alphabet\Capital\letter_J.png')
letter_K = pygame.image.load(r'.\Images\Alphabet\Capital\letter_K.png')
letter_L = pygame.image.load(r'.\Images\Alphabet\Capital\letter_L.png')
letter_M = pygame.image.load(r'.\Images\Alphabet\Capital\letter_M.png')
letter_N = pygame.image.load(r'.\Images\Alphabet\Capital\letter_N.png')
letter_O = pygame.image.load(r'.\Images\Alphabet\Capital\letter_O.png')
letter_P = pygame.image.load(r'.\Images\Alphabet\Capital\letter_P.png')
letter_Q = pygame.image.load(r'.\Images\Alphabet\Capital\letter_Q.png')
letter_R = pygame.image.load(r'.\Images\Alphabet\Capital\letter_R.png')
letter_S = pygame.image.load(r'.\Images\Alphabet\Capital\letter_S.png')
letter_T = pygame.image.load(r'.\Images\Alphabet\Capital\letter_T.png')
letter_U = pygame.image.load(r'.\Images\Alphabet\Capital\letter_U.png')
letter_V = pygame.image.load(r'.\Images\Alphabet\Capital\letter_v.png')
letter_W = pygame.image.load(r'.\Images\Alphabet\Capital\letter_W.png')
letter_X = pygame.image.load(r'.\Images\Alphabet\Capital\letter_X.png')
letter_Y = pygame.image.load(r'.\Images\Alphabet\Capital\letter_y.png')
letter_Z = pygame.image.load(r'.\Images\Alphabet\Capital\letter_Z.png')

# Numbers:
# number_0 = pygame.image.load(r'.\Images\Alphabet\number_0.png')
# number_1 = pygame.image.load(r'.\Images\Alphabet\number_1.png')
# number_2 = pygame.image.load(r'.\Images\Alphabet\number_2.png')
# number_3 = pygame.image.load(r'.\Images\Alphabet\number_3.png')
# number_4 = pygame.image.load(r'.\Images\Alphabet\number_4.png')
# number_5 = pygame.image.load(r'.\Images\Alphabet\number_5.png')
# number_6 = pygame.image.load(r'.\Images\Alphabet\number_6.png')
# number_7 = pygame.image.load(r'.\Images\Alphabet\number_7.png')
# number_8 = pygame.image.load(r'.\Images\Alphabet\number_8.png')
# number_9 = pygame.image.load(r'.\Images\Alphabet\number_9.png')


# Special Characteres: 
# spec_char_period = pygame.image.load(r'.\Images\Alphabet\spec_char_period.png')
# spec_char_underline = pygame.image.load(r'.\Images\Alphabet\spec_char_underline.png')
# spec_char_at = pygame.image.load(r'.\Images\Alphabet\spec_char_at.png')
# spec_char_hifen = pygame.image.load(r'.\Images\Alphabet\spec_char_hifen.png')


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

# Login Page Background:
login_page_original = pygame.image.load(r'.\Images\Background\login_page_original.png')

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
fast_comet_original = pygame.image.load(r'.\Images\Colliders\fast_comet_original_small.png')


# PowerUps:


# Planets:
planet_original = pygame.image.load(r'.\Images\Planets\planet_original.png')

# Spacecrafts:
ship_F5S4 = pygame.image.load(r'.\Images\Spacecrafts\Spacecraft_F5S4.png')


# -------------------------------- OBJECTS CLASSES --------------------------------------------- #




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
	collider_angle = degrees(atan(random_x/random_y))
	print("random:", random_x, random_y)
	rotated_collider = pygame.transform.rotate(fast_comet_original, collider_angle)
	screen.blit(rotated_collider, (random_x, random_y))

# Calculate Colliders' trajectory:
def collider_trajectory(init_values, step):
	'''Recieve two points in Carteisan system (2 doubles of tuples)
	and calclates the linear function which pass on them.

	Libraries importation required:
		    - randint ( from numpy import linspace )

	Parameters:
		- init_values (list) : [ x1, y1, x2, y2]
		- step (integer or float)

	Returns:
		- [xlist, ylist] (list of lists)
	'''
	# Loading values
	x1 = init_values[0]
	y1 = init_values[1]
	x2 = init_values[2]
	y2 = init_values[3]
	# Angular Coeficient:
	m = (y1 - y2)/(x1 - x2)
	# Linear Coeficient:
	b = y1 - m*x1
	# X and Y values list:
	counter = np.linspace(x1, x2, step)
	xlist = []
	ylist = []

	for val in counter:
		y_val = m*val + b
		xlist.append(val)
		ylist.append(y_val)

	return [xlist, ylist]


def GameInput():
	pass

def Collision():
	pass
# ------------------------------ OBJECTS CLASSES ---------------------------------------------- #


# Collider Class (Objects which must be reflected):
class Collider:
	"""
	"""
	def __init__(self, image, orientation, mode):
		"""Loading all pre-set configurations for the class methods

		Libraries importation required:
		    - randint ( from random import randint )
		    - degrees ( from math import degrees)
		    - atan    ( from math import atan)
		    - sin     ( from math import sin)
		    - cos     ( from math import cos )

		Parameters:
			- image       (pygame.Surface)
			- orientation (string)
			- mode        (string)
		"""
		# Configurating recieved parameters:
		self.image = image
		self.orientation = orientation
		self.mode = mode
		# Orientation classification:
		if self.orientation == 'w' or self.orientation == 'up':
			self.pos_x = randint(1, display_height)
			self.pos_y = -100
		if self.orientation == 'a' or self.orientation == 'left':
			self.pos_x = -100
			self.pos_y = randint(1, display_width)
		if self.orientation == 's' or self.orientation == 'down':
			self.pos_x = random.randint(1, display_height)
			self.pos_y = display_width
		if self.orientation == 'd' or self.orientation == 'right':
			self.pos_x = display_height
			self.pos_y = random.randint(1, display_width)
		# Rotation angle (used to rotate the image and make it pointing to the planets center):
		if self.orientation == 'a' or self.orientation == 'left' or self.orientation == 's' or self.orientation == 'down':
			self.angle = - degrees(atan((display_width/2 - self.pos_y)/(display_height/2 - self.pos_x))) + 180
		if self.orientation == 'd' or self.orientation == 'right' or self.orientation == 'w' or self.orientation == 'up':
			self.angle = - degrees(atan((display_width/2 - self.pos_y)/(display_height/2 - self.pos_x)))

		if self.mode == 'n' or self.mode == 'normal':
			self.speed = 10
		if self.mode == 'f' or self.mode == 'fast':
			self.speed = 5
		if self.mode == 's' or self.mode == 'ship':
			pass
		print('angle: ', self.angle)

		# Calculating trajectory:
		self.pos_index = 1
		self.trajectory = collider_trajectory([self.pos_x - display_height/2, - self.pos_y + display_width/2, 0, 0], step=self.speed*10)
		print(len((self.trajectory[0][:])))
		print(len((self.trajectory[1][:])))

	def display(self):
		'''Rotate image and show it on screen'''
		self.rotated_collider = pygame.transform.rotate(self.image, self.angle)
		screen.blit(self.rotated_collider, (display_height/2 + self.pos_x, display_width/2 - self.pos_y))

	def update_pos(self):
		'''Update Collider position (generating moviment)'''
		self.list_x = self.trajectory[0][:]
		self.list_y = self.trajectory[1][:]
		self.pos_x = self.list_x[self.pos_index]
		self.pos_y = self.list_y[self.pos_index]
		self.pos_index += 1
		print(self.pos_x, self.pos_y)
		if self.pos_index == (len(self.trajectory[0][:]) - 1):
			collision_planet()
	def collision_planet(self):
		if self.orientation == 'w' or self.orientation == 'up':
			self.pos_x = random.randint(1, display_height)
			self.pos_y = 0
		if self.orientation == 'a' or self.orientation == 'left':
			self.pos_x = 0
			self.pos_y = random.randint(1, display_width)
		if self.orientation == 's' or self.orientation == 'down':
			self.pos_x = random.randint(1, display_height)
			self.pos_y = display_width
		if self.orientation == 'd' or self.orientation == 'right':
			self.pos_x = display_height
			self.pos_y = random.randint(1, display_width)
		print('collision_on Barrirer')
				
	def collision(self):
		if self.pos_x < 100 and self.pos_y < 100:
			if self.orientation == 'w' or self.orientation == 'up':
				self.pos_x = random.randint(1, display_height)
				self.pos_y = 0
			if self.orientation == 'a' or self.orientation == 'left':
				self.pos_x = 0
				self.pos_y = random.randint(1, display_width)
			if self.orientation == 's' or self.orientation == 'down':
				self.pos_x = random.randint(1, display_height)
				self.pos_y = display_width
			if self.orientation == 'd' or self.orientation == 'right':
				self.pos_x = display_height
				self.pos_y = random.randint(1, display_width)
		print('collision_on Barrirer')



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


# ----------------------------------- POSITIONS ------------------------------------------------ #


# Buttons:
but_play_pos = [[int((display_height - 180)/2),
				 int((display_width - 180)/2)], 
				[int((display_height + 165)/2),
				 int((display_width + 180)/2)]]

but_logoff_pos = [[int(( 169 )/450*display_height),
				   int(( 146 )/800*display_width)], 
				  [int(( 169 + 109 )/450*display_height),
				   int(( 146 + 120 )/800*display_width)]]

but_volon_pos = [[int(( 338 )/450*display_height),
				  int(( 243 )/800*display_width)],
				 [int(( 338 + 106 )/450*display_height),
				  int(( 243 + 122 )/800*display_width)]]

but_voloff_pos = [[int(( 338 )/450*display_height),
  				   int(( 243 )/800*display_width)],
				  [int(( 338 + 106 )/450*display_height),
				   int(( 243 + 122 )/800*display_width)]]

but_profile_pos = [[int(( 2 )/450*display_height), 
				    int(( 243 )/800*display_width)],
				   [int(( 2 + 109 )/450*display_height), 
				    int(( 243 + 120 )/800*display_width)]]

but_pause_pos = [[int(( 375 )/450*display_height),
				  int(( 3 )/800*display_width)],
				 [int(( 375 + 73 )/450*display_height),
				  int(( 3 + 81 )/800*display_width)]]

but_pause_yes_pos = [[int(( 55 )/450*display_height),
					  int(( 347 )/800*display_width)],
					 [int(( 55 + 81 )/450*display_height),
					  int(( 347 + 92 )/800*display_width)]]

but_pause_no_pos = [[int(( 333 )/450*display_height),
					 int(( 347 )/800*display_width)],
				    [int(( 333 + 81 )/450*display_height),
				     int(( 347 + 93 )/800*display_width)]]

but_star_pos = [[int(( 169 )/450*display_height),
				 int(( 535 )/800*display_width)],
			    [int(( 169 + 110 )/450*display_height), 
			     int(( 535 + 121 )/800*display_width)]]

but_config_pos = [[int(( 338 )/450*display_height),
				   int(( 435 )/800*display_width)],
				  [int(( 338 + 110 )/450*display_height),
				   int(( 435 + 121 )/800*display_width)]]

but_store_pos = [[int(( -1 )/450*display_height),
				  int(( 437 )/800*display_width)],
				 [int(( -1 + 110 )/450*display_height),
				  int(( 437 + 121 )/800*display_width)]]

but_login_confirm = [[int(( 198 )/450*display_height),
					  int(( 488 )/800*display_width)],
					 [int(( 198 + 81 )/450*display_height),
					  int(( 488 + 92 )/800*display_width)]]

# Planets:
planet_pos = [[int((display_height - 121)/2),
			   int((display_width - 121)/2)],
			  [int((display_height + 121)/2),
			   int((display_width + 121)/2)]]

# Barrier X axis:
cursor_x_pos = orbital_trajectory(117)[:, 0] + int((display_height - 121)/2)

# Barrier Y axis:
cursor_y_pos = orbital_trajectory(117)[:, 1] + int((display_width - 121)/2)


# ------------------------------------- SIGN UP PAGE ---------------------------------------------- #


# Main loop
def SignUpPage():
	# Loading Home Page (showing all the elements which compose the menu):
	screen.blit(login_page_original, (0, 0))
	screen.blit(but_pause_yes, (but_login_confirm[0][0] , but_login_confirm[0][1]))
	
	# Screen Commands:
	signup_runner = True
	# Input selector key:
	username_control = True 
	useremail_control = True
	userpassword_control = True
	# User data list: 
	username_input = []
	useremail_input = []
	userpassword_input = []
	# Special Keys Controlers:
	shift_pressed = False
	# Main Loop:
	while signup_runner:	
		
		

		for event in pygame.event.get():
			# Quit Command (Calls 'GameEnd' function):
			if event.type == pygame.QUIT:
				GameEnd()
			# Keyboard Click Detection (and cosequential actions, depending where/what is clicked):
			if event.type == pygame.KEYDOWN:

			# Keyboard NUMBERS Input:
				# 0 Key Command:
				if event.key == pygame.K_0 or event.key == pygame.K_KP0:
					if username_control == True:
						username_input.append('0')
					if useremail_control == True:
						useremail_input.append('0')
					if userpassword_control == True:
						userpassword_input.append('0')
				# 1 Key Command:
				if event.key == pygame.K_1 or event.key == pygame.K_KP1:
					if username_control == True:
						username_input.append('1')
					if useremail_control == True:
						useremail_input.append('1')
					if userpassword_control == True:
						userpassword_input.append('1')
				# 2 Key Command:
				if event.key == pygame.K_2 or event.key == pygame.K_KP2:
					# At ('@') Input:
					if shift_press == True:
						if username_control == True:
							pass
						if useremail_control == True:
							useremail_input.append('@')
						if userpassword_control == True:
							pass
						shift_press = False
					# Two ('2') Input:
					else:
						if username_control == True:
							username_input.append('2')
						if useremail_control == True:
							useremail_input.append('2')
						if userpassword_control == True:
							userpassword_input.append('2')
				# 3 Key Command:
				if event.key == pygame.K_3 or event.key == pygame.K_KP3:
					if username_control == True:
						username_input.append('3')
					if useremail_control == True:
						useremail_input.append('3')
					if userpassword_control == True:
						userpassword_input.append('3')
				# 4 Key Command:
				if event.key == pygame.K_4 or event.key == pygame.K_KP4:
					if username_control == True:
						username_input.append('4')
					if useremail_control == True:
						useremail_input.append('4')
					if userpassword_control == True:
						userpassword_input.append('4')
				# 5 Key Command:
				if event.key == pygame.K_5 or event.key == pygame.K_KP5:
					if username_control == True:
						username_input.append('5')
					if useremail_control == True:
						useremail_input.append('5')
					if userpassword_control == True:
						userpassword_input.append('5')
				# 6 Key Command:
				if event.key == pygame.K_6 or event.key == pygame.K_KP6:
					if username_control == True:
						username_input.append('6')
					if useremail_control == True:
						useremail_input.append('6')
					if userpassword_control == True:
						userpassword_input.append('6')
				# 7 Key Command:
				if event.key == pygame.K_7 or event.key == pygame.K_KP7:
					if username_control == True:
						username_input.append('7')
					if useremail_control == True:
						useremail_input.append('7')
					if userpassword_control == True:
						userpassword_input.append('7')
				# 8 Key Command:
				if event.key == pygame.K_8 or event.key == pygame.K_KP8:
					if username_control == True:
						username_input.append('8')
					if useremail_control == True:
						useremail_input.append('8')
					if userpassword_control == True:
						userpassword_input.append('8')
				# 9 Key Command:
				if event.key == pygame.K_9 or event.key == pygame.K_KP9:
					if username_control == True:
						username_input.append('9')
					if useremail_control == True:
						useremail_input.append('9')
					if userpassword_control == True:
						userpassword_input.append('9')

			# Keyboard LETTERS Input:
				# A Key Command:
				if event.key == pygame.K_a:
					# A Capital ('A') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('A')
						if useremail_control == True:
							useremail_input.append('A')
						if userpassword_control == True:
							userpassword_input.append('A')
						shift_press = False
					# A Lowercase ('a') Input:
					else:
						if username_control == True:
							username_input.append('a')
						if useremail_control == True:
							useremail_input.append('a')
						if userpassword_control == True:
							userpassword_input.append('a')
				# B Key Command:
				if event.key == pygame.K_b:
					# B Capital ('B') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('B')
						if useremail_control == True:
							useremail_input.append('B')
						if userpassword_control == True:
							userpassword_input.append('B')
						shift_press = False
					# B Lowercase ('b') Input:
					else:
						if username_control == True:
							username_input.append('b')
						if useremail_control == True:
							useremail_input.append('b')
						if userpassword_control == True:
							userpassword_input.append('b')
				# C Key Command:
				if event.key == pygame.K_c:
					# C Capital ('C') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('C')
						if useremail_control == True:
							useremail_input.append('C')
						if userpassword_control == True:
							userpassword_input.append('C')
					# C Lowercase ('c') Input:
					else:
						if username_control == True:
							username_input.append('C')
						if useremail_control == True:
							useremail_input.append('C')
						if userpassword_control == True:
							userpassword_input.append('C')
				# D Key Command:
				if event.key == pygame.K_d:
					# D Capital ('D') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('D')
						if useremail_control == True:
							useremail_input.append('D')
						if userpassword_control == True:
							userpassword_input.append('D')
					# D Lowercase ('d') Input:
					else:
						if username_control == True:
							username_input.append('d')
						if useremail_control == True:
							useremail_input.append('d')
						if userpassword_control == True:
							userpassword_input.append('d')
				# E Key Command:
				if event.key == pygame.K_e:
					# E Capital ('E') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('E')
						if useremail_control == True:
							useremail_input.append('E')
						if userpassword_control == True:
							userpassword_input.append('E')
					# E Lowercase ('e') Input:
					else:
						if username_control == True:
							username_input.append('e')
						if useremail_control == True:
							useremail_input.append('e')
						if userpassword_control == True:
							userpassword_input.append('e')
				# F Key Command:
				if event.key == pygame.K_f:
					# F Capital ('F') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('F')
						if useremail_control == True:
							useremail_input.append('F')
						if userpassword_control == True:
							userpassword_input.append('F')
					# F Lowercase ('f') Input:
					else:
						if username_control == True:
							username_input.append('f')
						if useremail_control == True:
							useremail_input.append('f')
						if userpassword_control == True:
							userpassword_input.append('f')
				# G Key Command:
				if event.key == pygame.K_g:
					# G Capital ('G') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('G')
						if useremail_control == True:
							useremail_input.append('G')
						if userpassword_control == True:
							userpassword_input.append('G')
					# G Lowercase ('g') Input:
					else:
						if username_control == True:
							username_input.append('g')
						if useremail_control == True:
							useremail_input.append('g')
						if userpassword_control == True:
							userpassword_input.append('g')
				# H Key Command:
				if event.key == pygame.K_h:
					# H Capital ('H') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('H')
						if useremail_control == True:
							useremail_input.append('H')
						if userpassword_control == True:
							userpassword_input.append('H')
					# H Lowercase ('h') Input:
					else:
						if username_control == True:
							username_input.append('h')
						if useremail_control == True:
							useremail_input.append('h')
						if userpassword_control == True:
							userpassword_input.append('h')
				# I Key Command:
				if event.key == pygame.K_i:
					# I Capital ('I') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('I')
						if useremail_control == True:
							useremail_input.append('I')
						if userpassword_control == True:
							userpassword_input.append('I')
					# I Lowercase ('i') Input:
					else:
						if username_control == True:
							username_input.append('i')
						if useremail_control == True:
							useremail_input.append('i')
						if userpassword_control == True:
							userpassword_input.append('i')
				# J Key Command:
				if event.key == pygame.K_j:
					# J Capital ('J') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('J')
						if useremail_control == True:
							useremail_input.append('J')
						if userpassword_control == True:
							userpassword_input.append('J')
					# J Lowercase ('j') Input:
					else:
						if username_control == True:
							username_input.append('j')
						if useremail_control == True:
							useremail_input.append('j')
						if userpassword_control == True:
							userpassword_input.append('j')
				# K Key Command:
				if event.key == pygame.K_k:
					# K Capital ('K') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('K')
						if useremail_control == True:
							useremail_input.append('K')
						if userpassword_control == True:
							userpassword_input.append('K')
					# K Lowercase ('k') Input:
					else:
						if username_control == True:
							username_input.append('k')
						if useremail_control == True:
							useremail_input.append('k')
						if userpassword_control == True:
							userpassword_input.append('k')
				# L Key Command:
				if event.key == pygame.K_l:
					# L Capital ('L') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('L')
						if useremail_control == True:
							useremail_input.append('L')
						if userpassword_control == True:
							userpassword_input.append('L')
					# L Lowercase ('l') Input:
					else:
						if username_control == True:
							username_input.append('l')
						if useremail_control == True:
							useremail_input.append('l')
						if userpassword_control == True:
							userpassword_input.append('l')
				# M Key Command:
				if event.key == pygame.K_m:
					# M Capital ('M') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('M')
						if useremail_control == True:
							useremail_input.append('M')
						if userpassword_control == True:
							userpassword_input.append('M')
					# M Lowercase ('m') Input:
					else:
						if username_control == True:
							username_input.append('m')
						if useremail_control == True:
							useremail_input.append('m')
						if userpassword_control == True:
							userpassword_input.append('m')
				# N Key Command:
				if event.key == pygame.K_n:
					# N Capital ('N') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('N')
						if useremail_control == True:
							useremail_input.append('N')
						if userpassword_control == True:
							userpassword_input.append('N')
					# N Lowercase ('n') Input:
					else:
						if username_control == True:
							username_input.append('n')
						if useremail_control == True:
							useremail_input.append('n')
						if userpassword_control == True:
							userpassword_input.append('n')
				# O Key Command:
				if event.key == pygame.K_o:
					# O Capital ('O') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('O')
						if useremail_control == True:
							useremail_input.append('O')
						if userpassword_control == True:
							userpassword_input.append('O')
					# O Lowercase ('o') Input:
					else:
						if username_control == True:
							username_input.append('o')
						if useremail_control == True:
							useremail_input.append('o')
						if userpassword_control == True:
							userpassword_input.append('o')
				# P Key Command:
				if event.key == pygame.K_p:
					# P Capital ('P') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('P')
						if useremail_control == True:
							useremail_input.append('P')
						if userpassword_control == True:
							userpassword_input.append('P')
					# L Lowercase ('l') Input:
					else:
						if username_control == True:
							username_input.append('p')
						if useremail_control == True:
							useremail_input.append('p')
						if userpassword_control == True:
							userpassword_input.append('p')
				# Q Key Command:
				if event.key == pygame.K_q:
					# Q Capital ('Q') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('Q')
						if useremail_control == True:
							useremail_input.append('Q')
						if userpassword_control == True:
							userpassword_input.append('Q')
					# Q Lowercase ('q') Input:
					else:
						if username_control == True:
							username_input.append('q')
						if useremail_control == True:
							useremail_input.append('q')
						if userpassword_control == True:
							userpassword_input.append('q')
				# R Key Command:
				if event.key == pygame.K_r:
					# R Capital ('R') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('R')
						if useremail_control == True:
							useremail_input.append('R')
						if userpassword_control == True:
							userpassword_input.append('R')
					# R Lowercase ('r') Input:
					else:
						if username_control == True:
							username_input.append('r')
						if useremail_control == True:
							useremail_input.append('r')
						if userpassword_control == True:
							userpassword_input.append('r')
				# S Key Command:
				if event.key == pygame.K_s:
					# S Capital ('S') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('S')
						if useremail_control == True:
							useremail_input.append('S')
						if userpassword_control == True:
							userpassword_input.append('S')
					# S Lowercase ('s') Input:
					else:
						if username_control == True:
							username_input.append('s')
						if useremail_control == True:
							useremail_input.append('s')
						if userpassword_control == True:
							userpassword_input.append('s')
				# T Key Command:
				if event.key == pygame.K_t:
					# T Capital ('T') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('T')
						if useremail_control == True:
							useremail_input.append('T')
						if userpassword_control == True:
							userpassword_input.append('T')
					# T Lowercase ('t') Input:
					else:
						if username_control == True:
							username_input.append('t')
						if useremail_control == True:
							useremail_input.append('t')
						if userpassword_control == True:
							userpassword_input.append('t')
				# U Key Command:
				if event.key == pygame.K_u:
					# U Capital ('U') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('U')
						if useremail_control == True:
							useremail_input.append('U')
						if userpassword_control == True:
							userpassword_input.append('U')
					# U Lowercase ('u') Input:
					else:
						if username_control == True:
							username_input.append('u')
						if useremail_control == True:
							useremail_input.append('u')
						if userpassword_control == True:
							userpassword_input.append('u')
				# V Key Command:
				if event.key == pygame.K_v:
					# V Capital ('V') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('V')
						if useremail_control == True:
							useremail_input.append('V')
						if userpassword_control == True:
							userpassword_input.append('V')
					# V Lowercase ('v') Input:
					else:
						if username_control == True:
							username_input.append('v')
						if useremail_control == True:
							useremail_input.append('v')
						if userpassword_control == True:
							userpassword_input.append('v')
				# W Key Command:
				if event.key == pygame.K_w:
					# W Capital ('W') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('W')
						if useremail_control == True:
							useremail_input.append('W')
						if userpassword_control == True:
							userpassword_input.append('W')
					# W Lowercase ('w') Input:
					else:
						if username_control == True:
							username_input.append('w')
						if useremail_control == True:
							useremail_input.append('w')
						if userpassword_control == True:
							userpassword_input.append('w')
				# X Key Command:
				if event.key == pygame.K_x:
					# X Capital ('X') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('X')
						if useremail_control == True:
							useremail_input.append('X')
						if userpassword_control == True:
							userpassword_input.append('X')
					# X Lowercase ('x') Input:
					else:
						if username_control == True:
							username_input.append('x')
						if useremail_control == True:
							useremail_input.append('x')
						if userpassword_control == True:
							userpassword_input.append('x')
				# Y Key Command:
				if event.key == pygame.K_y:
					# Y Capital ('Y') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('Y')
						if useremail_control == True:
							useremail_input.append('Y')
						if userpassword_control == True:
							userpassword_input.append('Y')
					# Y Lowercase ('y') Input:
					else:
						if username_control == True:
							username_input.append('y')
						if useremail_control == True:
							useremail_input.append('y')
						if userpassword_control == True:
							userpassword_input.append('y')
				# Z Key Command:
				if event.key == pygame.K_z:
					# Z Capital ('Z') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('Z')
						if useremail_control == True:
							useremail_input.append('Z')
						if userpassword_control == True:
							userpassword_input.append('Z')
					# Z Lowercase ('z') Input:
					else:
						if username_control == True:
							username_input.append('z')
						if useremail_control == True:
							useremail_input.append('z')
						if userpassword_control == True:
							userpassword_input.append('z')

			# Keyboard OTHER CHARACTERES Input:
				# Space Key Command:
				if event.key == pygame.K_SPACE:
					# Space (' ') Input:		
					if username_control == True:
						username_input.append(' ')
					if useremail_control == True:
						pass
					if userpassword_control == True:
						pass
				# Dot Key Command:
				if event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
					# Dot Capital ('.') Input:
					if username_control == True:
						pass
					if useremail_control == True:
						useremail_input.append('.')
					if userpassword_control == True:
						userpassword_input.append('.')
				# Hifen Key Command:
				if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
					if username_control == True:
						pass
					if useremail_control == True:
						useremail_input.append('-')
					if userpassword_control == True:
						userpassword_input.append('-')

			# Keyborad SPECIAL KEYS Input:
				# Shift Keys Command:
				if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
					shift_press = True
					print('Shift pressed')
				# Enter Keys Command:
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
					print(username_input)
					print(useremail_input)
					print(userpassword_input)
				# Delete Last Letter Command:
				if event.key == pygame.K_BACKSPACE:
					if username_control == True:
						try:
							del username_input[-1]
						except:
							pass
					if useremail_control == True:
						try:
							del useremail_input[-1]
						except:
							pass
					if userpassword_control == True:
						try:
							del username_input[-1]
						except:
							pass
				# Exit Command:
				if event.key == pygame.K_ESCAPE:
					GameEnd()

		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)

# ------------------------------------- LOGIN PAGE ---------------------------------------------- #


# Main loop
def LoginPage():
	# Loading Home Page (showing all the elements which compose the menu):
	screen.blit(login_page_original, (0, 0))
	screen.blit(but_pause_yes, (but_login_confirm[0][0] , but_login_confirm[0][1]))
	
	# Screen Commands:
	login_runner = True
	# Input selector key:
	username_control = True 
	userpassword_control = True
	# User data list: 
	username_input = []
	userpassword_input = []
	# Special Keys Controlers:
	shift_press = False
	# Main Loop:
	while login_runner:	
		for event in pygame.event.get():
			# Quit Command (Calls 'GameEnd' function):
			if event.type == pygame.QUIT:
				GameEnd()
			# Keyboard Click Detection (and cosequential actions, depending where/what is clicked):
			if event.type == pygame.KEYDOWN:

			# Keyboard NUMBERS Input:
				# 0 Key Command:
				if event.key == pygame.K_0 or event.key == pygame.K_KP0:
					if username_control == True:
						username_input.append('0')
					if userpassword_control == True:
						userpassword_input.append('0')
				# 1 Key Command:
				if event.key == pygame.K_1 or event.key == pygame.K_KP1:
					if username_control == True:
						username_input.append('1')
					if userpassword_control == True:
						userpassword_input.append('1')
				# 2 Key Command:
				if event.key == pygame.K_2 or event.key == pygame.K_KP2:
					# At ('@') Input:
					if shift_press == True:
						if username_control == True:
							pass
						if userpassword_control == True:
							pass
						shift_press = False
					# Two ('2') Input:
					else:
						if username_control == True:
							username_input.append('2')
						if userpassword_control == True:
							userpassword_input.append('2')
				# 3 Key Command:
				if event.key == pygame.K_3 or event.key == pygame.K_KP3:
					if username_control == True:
						username_input.append('3')
					if userpassword_control == True:
						userpassword_input.append('3')
				# 4 Key Command:
				if event.key == pygame.K_4 or event.key == pygame.K_KP4:
					if username_control == True:
						username_input.append('4')
					if userpassword_control == True:
						userpassword_input.append('4')
				# 5 Key Command:
				if event.key == pygame.K_5 or event.key == pygame.K_KP5:
					if username_control == True:
						username_input.append('5')
					if userpassword_control == True:
						userpassword_input.append('5')
				# 6 Key Command:
				if event.key == pygame.K_6 or event.key == pygame.K_KP6:
					if username_control == True:
						username_input.append('6')
					if userpassword_control == True:
						userpassword_input.append('6')
				# 7 Key Command:
				if event.key == pygame.K_7 or event.key == pygame.K_KP7:
					if username_control == True:
						username_input.append('7')
					if userpassword_control == True:
						userpassword_input.append('7')
				# 8 Key Command:
				if event.key == pygame.K_8 or event.key == pygame.K_KP8:
					if username_control == True:
						username_input.append('8')
					if userpassword_control == True:
						userpassword_input.append('8')
				# 9 Key Command:
				if event.key == pygame.K_9 or event.key == pygame.K_KP9:
					if username_control == True:
						username_input.append('9')
					if userpassword_control == True:
						userpassword_input.append('9')

			# Keyboard LETTERS Input:
				# A Key Command:
				if event.key == pygame.K_a:
					# A Capital ('A') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('A')
						if userpassword_control == True:
							userpassword_input.append('A')
						shift_press = False
					# A Lowercase ('a') Input:
					else:
						if username_control == True:
							username_input.append('a')
						if userpassword_control == True:
							userpassword_input.append('a')
				# B Key Command:
				if event.key == pygame.K_b:
					# B Capital ('B') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('B')
						if userpassword_control == True:
							userpassword_input.append('B')
						shift_press = False
					# B Lowercase ('b') Input:
					else:
						if username_control == True:
							username_input.append('b')
						if userpassword_control == True:
							userpassword_input.append('b')
				# C Key Command:
				if event.key == pygame.K_c:
					# C Capital ('C') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('C')
						if userpassword_control == True:
							userpassword_input.append('C')
					# C Lowercase ('c') Input:
					else:
						if username_control == True:
							username_input.append('C')
						if userpassword_control == True:
							userpassword_input.append('C')
				# D Key Command:
				if event.key == pygame.K_d:
					# D Capital ('D') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('D')
						if userpassword_control == True:
							userpassword_input.append('D')
					# D Lowercase ('d') Input:
					else:
						if username_control == True:
							username_input.append('d')
						if userpassword_control == True:
							userpassword_input.append('d')
				# E Key Command:
				if event.key == pygame.K_e:
					# E Capital ('E') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('E')
						if userpassword_control == True:
							userpassword_input.append('E')
					# E Lowercase ('e') Input:
					else:
						if username_control == True:
							username_input.append('e')
						if userpassword_control == True:
							userpassword_input.append('e')
				# F Key Command:
				if event.key == pygame.K_f:
					# F Capital ('F') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('F')
						if userpassword_control == True:
							userpassword_input.append('F')
					# F Lowercase ('f') Input:
					else:
						if username_control == True:
							username_input.append('f')
						if userpassword_control == True:
							userpassword_input.append('f')
				# G Key Command:
				if event.key == pygame.K_g:
					# G Capital ('G') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('G')
						if userpassword_control == True:
							userpassword_input.append('G')
					# G Lowercase ('g') Input:
					else:
						if username_control == True:
							username_input.append('g')
						if userpassword_control == True:
							userpassword_input.append('g')
				# H Key Command:
				if event.key == pygame.K_h:
					# H Capital ('H') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('H')
						if userpassword_control == True:
							userpassword_input.append('H')
					# H Lowercase ('h') Input:
					else:
						if username_control == True:
							username_input.append('h')
						if userpassword_control == True:
							userpassword_input.append('h')
				# I Key Command:
				if event.key == pygame.K_i:
					# I Capital ('I') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('I')
						if userpassword_control == True:
							userpassword_input.append('I')
					# I Lowercase ('i') Input:
					else:
						if username_control == True:
							username_input.append('i')
						if userpassword_control == True:
							userpassword_input.append('i')
				# J Key Command:
				if event.key == pygame.K_j:
					# J Capital ('J') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('J')
						if userpassword_control == True:
							userpassword_input.append('J')
					# J Lowercase ('j') Input:
					else:
						if username_control == True:
							username_input.append('j')
						if userpassword_control == True:
							userpassword_input.append('j')
				# K Key Command:
				if event.key == pygame.K_k:
					# K Capital ('K') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('K')
						if userpassword_control == True:
							userpassword_input.append('K')
					# K Lowercase ('k') Input:
					else:
						if username_control == True:
							username_input.append('k')
						if userpassword_control == True:
							userpassword_input.append('k')
				# L Key Command:
				if event.key == pygame.K_l:
					# L Capital ('L') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('L')
						if userpassword_control == True:
							userpassword_input.append('L')
					# L Lowercase ('l') Input:
					else:
						if username_control == True:
							username_input.append('l')
						if userpassword_control == True:
							userpassword_input.append('l')
				# M Key Command:
				if event.key == pygame.K_m:
					# M Capital ('M') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('M')
						if userpassword_control == True:
							userpassword_input.append('M')
					# M Lowercase ('m') Input:
					else:
						if username_control == True:
							username_input.append('m')
						if userpassword_control == True:
							userpassword_input.append('m')
				# N Key Command:
				if event.key == pygame.K_n:
					# N Capital ('N') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('N')
						if userpassword_control == True:
							userpassword_input.append('N')
					# N Lowercase ('n') Input:
					else:
						if username_control == True:
							username_input.append('n')
						if userpassword_control == True:
							userpassword_input.append('n')
				# O Key Command:
				if event.key == pygame.K_o:
					# O Capital ('O') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('O')
						if userpassword_control == True:
							userpassword_input.append('O')
					# O Lowercase ('o') Input:
					else:
						if username_control == True:
							username_input.append('o')
						if userpassword_control == True:
							userpassword_input.append('o')
				# P Key Command:
				if event.key == pygame.K_p:
					# P Capital ('P') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('P')
						if userpassword_control == True:
							userpassword_input.append('P')
					# L Lowercase ('l') Input:
					else:
						if username_control == True:
							username_input.append('p')
						if userpassword_control == True:
							userpassword_input.append('p')
				# Q Key Command:
				if event.key == pygame.K_q:
					# Q Capital ('Q') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('Q')
						if userpassword_control == True:
							userpassword_input.append('Q')
					# Q Lowercase ('q') Input:
					else:
						if username_control == True:
							username_input.append('q')
						if userpassword_control == True:
							userpassword_input.append('q')
				# R Key Command:
				if event.key == pygame.K_r:
					# R Capital ('R') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('R')
						if userpassword_control == True:
							userpassword_input.append('R')
					# R Lowercase ('r') Input:
					else:
						if username_control == True:
							username_input.append('r')
						if userpassword_control == True:
							userpassword_input.append('r')
				# S Key Command:
				if event.key == pygame.K_s:
					# S Capital ('S') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('S')
						if userpassword_control == True:
							userpassword_input.append('S')
					# S Lowercase ('s') Input:
					else:
						if username_control == True:
							username_input.append('s')
						if userpassword_control == True:
							userpassword_input.append('s')
				# T Key Command:
				if event.key == pygame.K_t:
					# T Capital ('T') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('T')
						if userpassword_control == True:
							userpassword_input.append('T')
					# T Lowercase ('t') Input:
					else:
						if username_control == True:
							username_input.append('t')
						if userpassword_control == True:
							userpassword_input.append('t')
				# U Key Command:
				if event.key == pygame.K_u:
					# U Capital ('U') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('U')
						if userpassword_control == True:
							userpassword_input.append('U')
					# U Lowercase ('u') Input:
					else:
						if username_control == True:
							username_input.append('u')
						if userpassword_control == True:
							userpassword_input.append('u')
				# V Key Command:
				if event.key == pygame.K_v:
					# V Capital ('V') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('V')
						if userpassword_control == True:
							userpassword_input.append('V')
					# V Lowercase ('v') Input:
					else:
						if username_control == True:
							username_input.append('v')
						if userpassword_control == True:
							userpassword_input.append('v')
				# W Key Command:
				if event.key == pygame.K_w:
					# W Capital ('W') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('W')
						if userpassword_control == True:
							userpassword_input.append('W')
					# W Lowercase ('w') Input:
					else:
						if username_control == True:
							username_input.append('w')
						if userpassword_control == True:
							userpassword_input.append('w')
				# X Key Command:
				if event.key == pygame.K_x:
					# X Capital ('X') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('X')
						if useremail_control == True:
							useremail_input.append('X')
						if userpassword_control == True:
							userpassword_input.append('X')
					# X Lowercase ('x') Input:
					else:
						if username_control == True:
							username_input.append('x')
						if useremail_control == True:
							useremail_input.append('x')
						if userpassword_control == True:
							userpassword_input.append('x')
				# Y Key Command:
				if event.key == pygame.K_y:
					# Y Capital ('Y') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('Y')
						if userpassword_control == True:
							userpassword_input.append('Y')
					# Y Lowercase ('y') Input:
					else:
						if username_control == True:
							username_input.append('y')
						if userpassword_control == True:
							userpassword_input.append('y')
				# Z Key Command:
				if event.key == pygame.K_z:
					# Z Capital ('Z') Input:
					if shift_press == True:
						if username_control == True:
							username_input.append('Z')
						if userpassword_control == True:
							userpassword_input.append('Z')
					# Z Lowercase ('z') Input:
					else:
						if username_control == True:
							username_input.append('z')
						if userpassword_control == True:
							userpassword_input.append('z')

			# Keyboard OTHER CHARACTERES Input:
				# Space Key Command:
				if event.key == pygame.K_SPACE:
					# Space (' ') Input:		
					if username_control == True:
						username_input.append(' ')
					if userpassword_control == True:
						pass
				# Dot Key Command:
				if event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
					# Dot Capital ('.') Input:
					if username_control == True:
						pass
					if userpassword_control == True:
						userpassword_input.append('.')
				# Hifen Key Command:
				if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
					if username_control == True:
						pass
					if userpassword_control == True:
						userpassword_input.append('-')

			# Keyborad SPECIAL KEYS Input:
				# Shift Keys Command:
				if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
					shift_press = True
					print('Shift pressed')

				# Enter Keys Command:
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
					print(username_input)
					print(userpassword_input)

				# Delete Last Letter Command:
				if event.key == pygame.K_BACKSPACE:
					if username_control == True:
						try:
							del username_input[-1]
						except:
							pass
					if userpassword_control == True:
						try:
							del userpassword_input[-1]
						except:
							pass
		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)


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
			# Mouse Click Detection (and consequential actions, depending where/what is clicked):
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
					return False
#	if exit_trigger == False:
#		return False
		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)


def ProfilePage():
	# Loop Controler:
	profile_runner = True
	# Profile Loop:
	while profile_runner:
		screen.blit(game_space, (0, 0))
		# Screen commands:
		for event in pygame.event.get():
			# Quit Command (Calls 'GameEnd' function): 
			if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
				profile_runner = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				# Mouse Position (axis x and -y coordinates):
				mouse_pos_x, mouse_pos_y = event.pos
				# Mouse Tracking:
				print(mouse_pos_x, mouse_pos_y)




		# Atualizating Screen:
		pygame.display.update()
		# Frame Rate Update (current rate: 60fps):
		clock.tick(60)


def LoadingPage():
	pass  


# -------------------------------------- GAME PAGE ---------------------------------------------- #

def GamePage():
	# Loop Controler:
	game_runner = True
	# Movement Delayer (Used to delay animation movement speed avoiding user visual discomfort):
	ticker = 0
	# 
	planet_HP = 1000
	# Rotation/Translation Controlers:
	planet_angle = 0
	barrier_angle = 0
	index_barrier_pos = 0
	barrier_runner = True
	# Colliders pre-settings:
	coll00 = Collider(fast_comet_original, 'd', 'n')
	coll01 = Collider(fast_comet_original, 'a', 'n')
	coll02 = Collider(fast_comet_original, 's', 'n')
	coll03 = Collider(fast_comet_original, 'd', 'n')

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
		coll00.display()

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
					pause_returned = PausePage()	
					if pause_returned == False:
						game_runner = False
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
#		if pygame.sprite.collide_circle(rotating_planet.get_rect(), rotating_barrier.get_rect()) == True:
#			print("Collision Detected")
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
			barrier_angle += 2
			index_barrier_pos -= 2
		elif barrier_runner == False:
			barrier_angle -= 2
			index_barrier_pos += 2	
		# Barrier Continuous Translation (reset index position counter):
		if index_barrier_pos < 0:
			index_barrier_pos = len(cursor_x_pos) - 1
		if index_barrier_pos > len(cursor_x_pos) - 1:
			index_barrier_pos = 0
		# Rate Command Control (check pressed buttons each 3 loop cycles):
		if ticker >= 3:
			ticker = 0
			coll00.update_pos()
		else:
			ticker += 1


# -------------------------------------- GAME END ---------------------------------------------- #


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
