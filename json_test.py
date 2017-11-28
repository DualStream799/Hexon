import json

players_data = json.loads(open('Players Data/master_player.json').read())
print(players_data)

input_username = input("Insert Username: ")
input_password = input("Insert Password: ")


try:
	players_data[input_username]
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


