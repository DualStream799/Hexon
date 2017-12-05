import json
from pprint import pprint

# Loading and reading JSON file:
with open('Players Data/players_profile.json') as json_file:
	players_data = json.load(json_file)

pprint(players_data)
# Inputs:
input_username = input("Insert Username: ")
input_password = input("Insert Password: ")

# Loop 1:
try:
	players_data[input_username]
	# Loop 2:
	try:
		players_data[input_username][input_password]
	except KeyError:
		print("Invalid Password")
	except Exception:
		print("Unknown error\nPlease contact support")

except KeyError:
	print("Invalid Username")
except Exception:
		print("Unknown error\nPlease contact support")


new_username = input("Insert new username: ")
new_password = input("Insert new password: ")
new_email = input("insert new email: ")

players_data[new_username] = {new_password: {'Email': new_email,
											 'HX$': 0,
											 'HighScore': 0,
											 'XP': 0,
											 'Level': 0,
											 'Etatus': 'Player',
											 'TimePlayed': 0}}
pprint(players_data)

with open('Players Data/players_profile.json', 'w') as json_file:
	json.dump(players_data, json_file)
	