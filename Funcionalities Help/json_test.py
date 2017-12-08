import json
import pygame
from pprint import pprint

"""# Loading and reading JSON file:
with open('Players Data/players_profile.json') as json_file:
	players_data = json.load(json_file)

pprint(players_data)

# Trying to log in:
try:
	input_username = input("Insert Username: ")
	players_data[input_username]
	try:
		input_password = input("Insert Password: ")
		players_data[input_username][input_password]
	except KeyError:
		print("Invalid Password")
	except Exception:
		print("Unknown error\nPlease contact support")

except KeyError:
	print("Invalid Username")
except Exception:
		print("Unknown error\nPlease contact support")

# Inputs:
new_username = input("Insert new username: ")
new_password = input("Insert new password: ")
new_email = input("insert new email: ")
# Organizing new data in JSON format(a dictionary of dictionaries):
players_data[new_username] = {new_password: {'Email': new_email,
											 'HX$': 0,
											 'HighScore': 0,
											 'XP': 0,
											 'Level': 0,
											 'Status': 'Player',
											 'TimePlayed': 0}}

# Saving data on JSON file:
with open('Players Data/players_profile.json', 'w') as json_file:
	json.dump(players_data, json_file)

"""


class PlayersData(object):
	""""""
	def __init__(self):
		"""Loading and reading JSON file:"""
		with open('../Players Data/players_profile.json') as json_file:
			self.players_data = json.load(json_file)
	
	def log_player(self, input_username, input_password):
		"""Trying to connect with database, check data and log in"""
		try:
			self.players_data[input_username]
			print('username accepted')
			try:	
				self.players_data[input_username][input_password]
				print('password accepted')
				print('logged')
			except KeyError:
				print("Invalid Password")
			except Exception:
				print("Unknown error\nPlease contact support")

		except KeyError:
			print("Invalid Username")
		except Exception:
				print("Unknown error\nPlease contact support")


	def load_new_player(self, new_username, new_email, new_password):
		"""Organizing new data in JSON format (a dictionary of dictionaries):"""
		self.players_data[new_username] = {new_password: {'Email': new_email,
													   	  'HX$': 0,
														  'HighScore': 0,
														  'XP': 0,
														  'Level': 0,
														  'Status': 'Player',
														  'TimePlayed': 0}}

	def saveJSON(self):
		"""Loading and saving data on JSON file:"""
		with open('../Players Data/players_profile.json', 'w') as json_file:
			json.dump(self.players_data, json_file)

# PlayersData().log_player('DualStream799', 'DualStream799')
print(help(pygame.sprite.collide_circle))