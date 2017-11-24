# -*- coding: utf-8 -*-
"""
Project: Hexon
Created on Tue Oct 24 16:4:15 2017
Current Version: 1.0.0
@author: dualstream799

"""

# ------------------------------------ LIBRARIES ------------------------------------------------ #

# Used:
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
pygame.display.set_caption('Hexon v1.0', 'hex_logo_small.png')
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


# PowerUps:


# Planets:
planet_original = pygame.image.load(r'.\Images\Planets\planet_original.png')

# Spacecrafts:
ship_F5S4 = pygame.image.load(r'.\Images\Spacecrafts\Spacecraft_F5S4.png')

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

"""
but_config_pos = [[2, 243], [2 + 109, 243 + 120]]
but_contact_pos = [[2, 243], [2 + 109, 243 + 120]]
"""


# Planets:
planet_pos = [[int((display_height - 121)/2), int((display_width - 121)/2)], [int((display_height + 121)/2), int((display_width + 121)/2)]]

# Barrier X axis:
cursor_x_pos = np.array([115.0, 92.0, 32.0, -42.0, -97.0, -110.0, -74.0, -6.0, 65.0, 109.0, 109.0, 66.0, -5.0, -73.0, -109.0, -98.0, 
						 -43.0, 30.0, 91.0, 115.0, 93.0, 33.0, -41.0, -96.0, -110.0, -75.0, -7.0, 64.0, 109.0, 110.0, 67.0, -4.0, -72.0, 
						 -109.0, -98.0, -44.0, 29.0, 90.0, 115.0, 93.0, 34.0, -39.0, -96.0, -110.0, -76.0, -8.0, 63.0, 108.0, 110.0, 68.0, 
						 -2.0, -71.0, -109.0, -99.0, -45.0, 28.0, 90.0, 115.0, 94.0, 35.0, -38.0, -95.0, -110.0, -77.0, -10.0, 62.0, 108.0, 
						 110.0, 69.0, -1.0, -70.0, -109.0, -99.0, -46.0, 27.0, 89.0, 115.0, 95.0, 36.0, -37.0, -94.0, -110.0, -78.0, -11.0, 
						 61.0, 107.0, 111.0, 70.0, 0.0, -69.0, -108.0, -100.0, -47.0, 26.0, 88.0, 115.0, 96.0, 37.0, -36.0, -94.0, -111.0, 
						 -78.0, -12.0, 59.0, 107.0, 111.0, 71.0, 1.0, -68.0, -108.0, -100.0, -49.0, 24.0, 87.0, 115.0, 96.0, 39.0, -35.0, 
						 -93.0, -111.0, -79.0, -13.0, 58.0, 106.0, 111.0, 72.0, 3.0, -67.0, -108.0, -101.0, -50.0, 23.0, 87.0, 115.0, 97.0, 
						 40.0, -34.0, -92.0, -111.0, -80.0, -15.0, 57.0, 106.0, 112.0, 73.0, 4.0, -66.0, -108.0, -101.0, -51.0, 22.0, 86.0, 
						 115.0, 98.0, 41.0, -32.0, -92.0, -111.0, -81.0, -16.0, 56.0, 105.0, 112.0, 74.0, 5.0, -65.0, -107.0, -102.0, -52.0, 
						 21.0, 85.0, 115.0, 98.0, 42.0, -31.0, -91.0, -111.0, -82.0, -17.0, 55.0, 105.0, 112.0, 74.0, 6.0, -64.0, -107.0, 
						 -102.0, -53.0, 20.0, 84.0, 114.0, 99.0, 43.0, -30.0, -90.0, -111.0, -83.0, -18.0, 54.0, 104.0, 113.0, 75.0, 8.0, 
						 -63.0, -107.0, -103.0, -54.0, 18.0, 83.0, 114.0, 99.0, 44.0, -29.0, -90.0, -111.0, -84.0, -20.0, 53.0, 104.0, 113.0, 
						 76.0, 9.0, -62.0, -106.0, -103.0, -55.0, 17.0, 82.0, 114.0, 100.0, 46.0, -28.0, -89.0, -111.0, -84.0, -21.0, 52.0, 
						 103.0, 113.0, 77.0, 10.0, -61.0, -106.0, -104.0, -56.0, 16.0, 81.0, 114.0, 101.0, 47.0, -26.0, -88.0, -111.0, -85.0, 
						 -22.0, 51.0, 103.0, 113.0, 78.0, 11.0, -60.0, -105.0, -104.0, -57.0, 15.0, 81.0, 114.0, 101.0, 48.0, -25.0, -87.0, 
						 -111.0, -86.0, -23.0, 50.0, 102.0, 113.0, 79.0, 13.0, -59.0, -105.0, -105.0, -58.0, 13.0, 80.0, 114.0, 102.0, 49.0, 
						 -24.0, -87.0, -111.0, -87.0, -24.0, 49.0, 102.0, 114.0, 80.0, 14.0, -58.0, -105.0, -105.0, -59.0, 12.0, 79.0, 113.0, 
						 102.0, 50.0, -23.0, -86.0, -111.0, -88.0, -26.0, 47.0, 101.0, 114.0, 81.0, 15.0, -57.0, -104.0, -106.0, -60.0, 11.0, 
						 78.0, 113.0, 103.0, 51.0, -22.0, -85.0, -111.0, -88.0, -27.0, 46.0, 100.0, 114.0, 82.0, 16.0, -56.0, -104.0, -106.0, 
						 -61.0, 10.0, 77.0, 113.0, 103.0, 52.0, -20.0, -84.0, -111.0, -89.0, -28.0, 45.0, 100.0, 114.0, 83.0, 17.0, -55.0, 
						 -103.0, -106.0, -63.0, 8.0, 76.0, 113.0, 104.0, 53.0, -19.0, -83.0, -111.0, -90.0, -29.0, 44.0, 99.0, 114.0, 83.0, 
						 19.0, -54.0, -103.0, -107.0, -64.0, 7.0, 75.0, 112.0, 105.0, 54.0, -18.0, -83.0, -111.0, -91.0, -30.0, 43.0, 99.0, 
						 114.0, 84.0, 20.0, -53.0, -102.0, -107.0, -65.0, 6.0, 74.0, 112.0, 105.0, 56.0, -17.0, -82.0, -111.0, -91.0, -32.0, 
						 42.0, 98.0, 115.0, 85.0, 21.0, -52.0, -102.0, -107.0, -66.0, 5.0, 73.0, 112.0, 106.0, 57.0, -15.0, -81.0, -111.0, 
						 -92.0, -33.0, 41.0, 97.0, 115.0, 86.0, 22.0, -50.0, -101.0, -108.0, -67.0, 4.0, 72.0, 112.0, 106.0, 58.0, -14.0, 
						 -80.0, -111.0, -93.0, -34.0, 39.0, 97.0, 115.0, 87.0, 24.0, -49.0, -101.0, -108.0, -68.0, 2.0, 71.0, 111.0, 106.0, 
						 59.0, -13.0, -79.0, -111.0, -93.0, -35.0, 38.0, 96.0, 115.0, 88.0, 25.0, -48.0, -100.0, -108.0, -69.0, 1.0, 70.0, 
						 111.0, 107.0, 60.0, -12.0, -78.0, -110.0, -94.0, -36.0, 37.0, 95.0, 115.0, 88.0, 26.0, -47.0, -100.0, -109.0, -70.0, 
						 -0.0, 69.0, 111.0, 107.0, 61.0, -11.0, -77.0, -110.0, -95.0, -37.0, 36.0, 95.0, 115.0, 89.0, 27.0, -46.0, -99.0, 
						 -109.0, -70.0, -1.0, 68.0, 110.0, 108.0, 62.0, -9.0, -76.0, -110.0, -95.0, -39.0, 35.0, 94.0, 115.0, 90.0, 28.0, 
						 -45.0, -99.0, -109.0, -71.0, -3.0, 67.0, 110.0, 108.0, 63.0, -8.0, -75.0, -110.0, -96.0, -40.0, 34.0, 93.0, 115.0, 
						 91.0, 30.0, -44.0, -98.0, -109.0, -72.0, -4.0, 66.0, 110.0, 109.0, 64.0, -7.0, -75.0, -110.0, -97.0, -41.0, 32.0, 
						 92.0, 115.0, 91.0, 31.0, -43.0, -97.0, -110.0, -73.0, -5.0, 65.0, 109.0, 109.0, 65.0, -6.0, -74.0, -110.0, -97.0, 
						 -42.0, 31.0, 92.0]) + int(display_height - 25)/2

# Barrier Y axis:
cursor_y_pos = np.array([0.0, 69.0, 109.0, 104.0, 55.0, -19.0, -84.0, -113.0, -94.0, -37.0, 36.0, 93.0, 113.0, 85.0, 20.0, -54.0, -104.0, 
						 -109.0, -69.0, -1.0, 68.0, 109.0, 105.0, 56.0, -17.0, -83.0, -113.0, -95.0, -38.0, 34.0, 93.0, 113.0, 86.0, 21.0, 
						 -53.0, -103.0, -110.0, -70.0, -2.0, 67.0, 108.0, 105.0, 57.0, -16.0, -82.0, -113.0, -95.0, -39.0, 33.0, 92.0, 113.0, 
						 86.0, 22.0, -52.0, -103.0, -110.0, -71.0, -4.0, 66.0, 108.0, 106.0, 58.0, -15.0, -81.0, -113.0, -96.0, -40.0, 32.0, 
						 91.0, 113.0, 87.0, 24.0, -50.0, -102.0, -110.0, -72.0, -5.0, 65.0, 108.0, 106.0, 59.0, -14.0, -80.0, -112.0, -97.0, 
						 -41.0, 31.0, 91.0, 113.0, 88.0, 25.0, -49.0, -102.0, -111.0, -73.0, -6.0, 64.0, 107.0, 107.0, 60.0, -12.0, -80.0, 
						 -112.0, -97.0, -42.0, 30.0, 90.0, 113.0, 89.0, 26.0, -48.0, -101.0, -111.0, -74.0, -7.0, 63.0, 107.0, 107.0, 61.0, 
						 -11.0, -79.0, -112.0, -98.0, -44.0, 29.0, 89.0, 113.0, 90.0, 27.0, -47.0, -101.0, -111.0, -75.0, -9.0, 62.0, 107.0, 
						 107.0, 62.0, -10.0, -78.0, -112.0, -99.0, -45.0, 27.0, 88.0, 113.0, 90.0, 28.0, -46.0, -100.0, -111.0, -76.0, -10.0, 
						 60.0, 106.0, 108.0, 63.0, -9.0, -77.0, -112.0, -99.0, -46.0, 26.0, 88.0, 113.0, 91.0, 30.0, -45.0, -100.0, -112.0, 
						 -77.0, -11.0, 59.0, 106.0, 108.0, 64.0, -7.0, -76.0, -112.0, -100.0, -47.0, 25.0, 87.0, 113.0, 92.0, 31.0, -44.0, 
						 -99.0, -112.0, -78.0, -12.0, 58.0, 105.0, 109.0, 66.0, -6.0, -75.0, -111.0, -100.0, -48.0, 24.0, 86.0, 113.0, 93.0, 
						 32.0, -42.0, -98.0, -112.0, -79.0, -13.0, 57.0, 105.0, 109.0, 67.0, -5.0, -74.0, -111.0, -101.0, -49.0, 23.0, 85.0, 
						 113.0, 93.0, 33.0, -41.0, -98.0, -112.0, -80.0, -15.0, 56.0, 104.0, 109.0, 68.0, -4.0, -73.0, -111.0, -101.0, -50.0, 
						 21.0, 84.0, 113.0, 94.0, 35.0, -40.0, -97.0, -112.0, -80.0, -16.0, 55.0, 104.0, 110.0, 69.0, -2.0, -72.0, -111.0, 
						 -102.0, -51.0, 20.0, 84.0, 113.0, 95.0, 36.0, -39.0, -96.0, -112.0, -81.0, -17.0, 54.0, 103.0, 110.0, 70.0, -1.0, 
						 -71.0, -110.0, -103.0, -52.0, 19.0, 83.0, 113.0, 95.0, 37.0, -38.0, -96.0, -113.0, -82.0, -18.0, 53.0, 103.0, 110.0, 
						 71.0, 0.0, -70.0, -110.0, -103.0, -53.0, 18.0, 82.0, 112.0, 96.0, 38.0, -37.0, -95.0, -113.0, -83.0, -19.0, 52.0, 
						 102.0, 110.0, 71.0, 1.0, -69.0, -110.0, -104.0, -55.0, 17.0, 81.0, 112.0, 97.0, 39.0, -35.0, -94.0, -113.0, -84.0, 
						 -21.0, 51.0, 102.0, 111.0, 72.0, 3.0, -68.0, -109.0, -104.0, -56.0, 15.0, 80.0, 112.0, 97.0, 40.0, -34.0, -94.0, 
						 -113.0, -85.0, -22.0, 50.0, 101.0, 111.0, 73.0, 4.0, -67.0, -109.0, -105.0, -57.0, 14.0, 79.0, 112.0, 98.0, 42.0, 
						 -33.0, -93.0, -113.0, -85.0, -23.0, 49.0, 101.0, 111.0, 74.0, 5.0, -66.0, -109.0, -105.0, -58.0, 13.0, 78.0, 112.0, 
						 99.0, 43.0, -32.0, -92.0, -113.0, -86.0, -24.0, 48.0, 100.0, 111.0, 75.0, 6.0, -65.0, -108.0, -105.0, -59.0, 12.0, 
						 78.0, 112.0, 99.0, 44.0, -31.0, -92.0, -113.0, -87.0, -25.0, 47.0, 100.0, 112.0, 76.0, 8.0, -64.0, -108.0, -106.0, 
						 -60.0, 11.0, 77.0, 111.0, 100.0, 45.0, -29.0, -91.0, -113.0, -88.0, -27.0, 45.0, 99.0, 112.0, 77.0, 9.0, -63.0, 
						 -108.0, -106.0, -61.0, 9.0, 76.0, 111.0, 100.0, 46.0, -28.0, -90.0, -113.0, -89.0, -28.0, 44.0, 98.0, 112.0, 78.0, 
						 10.0, -62.0, -107.0, -107.0, -62.0, 8.0, 75.0, 111.0, 101.0, 47.0, -27.0, -89.0, -113.0, -89.0, -29.0, 43.0, 98.0, 
						 112.0, 79.0, 12.0, -61.0, -107.0, -107.0, -63.0, 7.0, 74.0, 111.0, 101.0, 49.0, -26.0, -89.0, -113.0, -90.0, -30.0, 
						 42.0, 97.0, 112.0, 80.0, 13.0, -60.0, -106.0, -107.0, -64.0, 6.0, 73.0, 111.0, 102.0, 50.0, -24.0, -88.0, -113.0, 
						 -91.0, -31.0, 41.0, 97.0, 112.0, 81.0, 14.0, -59.0, -106.0, -108.0, -65.0, 4.0, 72.0, 110.0, 103.0, 51.0, -23.0, 
						 -87.0, -113.0, -92.0, -32.0, 40.0, 96.0, 113.0, 82.0, 15.0, -58.0, -106.0, -108.0, -66.0, 3.0, 71.0, 110.0, 103.0, 
						 52.0, -22.0, -86.0, -113.0, -92.0, -34.0, 39.0, 95.0, 113.0, 82.0, 17.0, -57.0, -105.0, -109.0, -67.0, 2.0, 70.0, 
						 110.0, 104.0, 53.0, -21.0, -85.0, -113.0, -93.0, -35.0, 37.0, 95.0, 113.0, 83.0, 18.0, -56.0, -105.0, -109.0, -68.0, 
						 1.0, 69.0, 109.0, 104.0, 54.0, -19.0, -84.0, -113.0, -94.0, -36.0, 36.0, 94.0, 113.0, 84.0, 19.0, -55.0, -104.0, 
						 -109.0, -69.0]) + int(display_width - 42)/2


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
			if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
				GameEnd()
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
	planet_angle = 0
	barrier_angle = 0
	index_barrier_pos = 0
	index_barrier_runner = True
	# ticker is used to delay our animation
	ticker = 0
	# Game Loop
	while game_runner:
		rotating_planet = image_rotation_centered(planet_original, planet_angle)
		rotating_barrier = image_rotation_centered(cursor_purple, barrier_angle)
		# Loading Home Page (showing all the elements which compose the menu):
		screen.blit(game_space, (0, 0))
		screen.blit(but_pause, (but_pause_pos[0][0], but_pause_pos[0][1])) 
		screen.blit(planet_original, (planet_pos[0][0], planet_pos[0][1]))
		screen.blit(rotating_planet, (planet_pos[0][0], planet_pos[0][1]))
		screen.blit(cursor_purple, (cursor_x_pos[index_barrier_pos], cursor_y_pos[index_barrier_pos]))
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
				if event.key == pygame.K_a:
					index_barrier_runner = False
					print(index_barrier_pos)
				# ANTICLOCKWISE Barrier Command (Make Barrier rotate to the left):
				if event.key == pygame.K_d:
					index_barrier_runner = True
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

		# Planet Continuous Rotation (reset barrier angle counter):
		if barrier_angle >= 360:
			barrier_angle = 0
		else:
			barrier_angle += 2


		if ticker >= 3:
			if index_barrier_runner == True:
				index_barrier_pos -= 1
			elif index_barrier_runner == False:
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
