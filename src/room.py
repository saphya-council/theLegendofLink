import json
import music21
from player import *
from musescore_midi import *

def get_room(id):
	#global ret = None
	ret = None
	
	if area["forest_visited"] == "1":
		if player_equip["equipped"] == "map":
			with open("../forest/rooms_map/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		else:

			if player_equip["equipped"] == "rupees":
				with open("../forest/rooms_rupees/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)
			
			elif player_equip["equipped"] == "blue ring":
				with open("../forest/rooms_ring/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)
				
			elif player_equip["equipped"] == "letter":
				with open("../forest/rooms_letter/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)
				
			elif player_equip["equipped"] == "food":
				with open("../forest/rooms_food/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)
		
			elif player_equip["shield"] == "wooden shield":
				with open("../forest/rooms_woodshield/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)
				
			elif player_equip["shield"] == "magical shield":
				with open("../forest/rooms_magshield/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)

			
			elif player_equip["sword"] == "wooden sword":
				with open("../forest/rooms_woodsword/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)
					
			elif player_equip["sword"] == "white sword":
				with open("../forest/rooms_whitesword/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)

			elif player_equip["sword"] == "magical sword":
				with open("../forest/rooms_magsword/"+str(id)+".json", "r") as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)
					
			else:
				with open("../forest/rooms/"+str(id)+".json", 'r') as f:
					jsontext = f.read()
					d = json.loads(jsontext)
					d['id'] = id
					ret = Room(**d)

			translate_midi(new_song,note_list,id)

			return ret

	elif area["merchant_visited"] == "1":
		if player_equip["equipped"] == "map":
			with open("../merchant/rooms_map/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)

		elif player_equip["equipped"] == "rupees":
			with open("../merchant/rooms_rupees/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		
		elif player_equip["equipped"] == "blue ring":
			with open("../merchant/rooms_ring/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
			
		elif player_equip["equipped"] == "letter":
			with open("../merchant/rooms_letter/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
			
		elif player_equip["equipped"] == "food":
			with open("../merchant/rooms_food/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)

		
		elif player_equip["shield"] == "wooden shield":
			with open("../merchant/rooms_woodshield/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
			
		elif player_equip["shield"] == "magical shield":
			with open("../merchant/rooms_magshield/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)

		
		elif player_equip["sword"] == "wooden sword":
			with open("../merchant/rooms_woodsword/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
				
		elif player_equip["sword"] == "white sword":
			with open("../merchant/rooms_whitesword/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)

		elif player_equip["sword"] == "magical sword":
			with open("../merchant/rooms_magsword/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
				
		else:
			with open("../merchant/rooms/"+str(id)+".json", 'r') as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)

		translate_midi(new_song,note_list,id)

		return ret

	else:
		#crosschecks inventory to cycle through specific events
		if player_equip["equipped"] == "rupees":
			with open("../default/rooms_rupees/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		elif player_equip["equipped"] == "blue ring":
			with open("../default/rooms_ring/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		elif player_equip["equipped"] == "letter":
			with open("../default/rooms_letter/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		elif player_equip["equipped"] == "food":
			with open("../default/rooms_food/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		
		elif player_equip["shield"] == "wooden shield":
			with open("../default/rooms_woodshield/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		elif player_equip["shield"] == "magical shield":
			with open("../default/rooms_magshield/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		
		elif player_equip["sword"] == "wooden sword":
			with open("../default/rooms_woodsword/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		elif player_equip["sword"] == "white sword":
			with open("../default/rooms_whitesword/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		elif player_equip["sword"] == "magical sword":
			with open("../default/rooms_magsword/"+str(id)+".json", "r") as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)
		else:
			with open("../default/rooms/"+str(id)+".json", 'r') as f:
				jsontext = f.read()
				d = json.loads(jsontext)
				d['id'] = id
				ret = Room(**d)

		translate_midi(new_song,note_list,id)

		return ret

class Room():

	#command = ''
	#resets 
	def __init__(self, id=0, name="A Room", description="An empty room", neighbors={}, equipped="", sword="", shield=""):
		self.id = id
		self.name = name
		self.description = description
		self.neighbors = neighbors
		self.equipped = equipped
		self.swords = sword
		self.shields = shield

	#update player location
	def _neighbor(self, direction):
		"""
		direction = direction.lower()
		print("The direction is: " + direction)
		"""
		if direction in self.neighbors:
			return self.neighbors[direction]
		else:
			return None

	def run(self):
		return self._neighbor(command)

	# def north(self):
	# 	return self._neighbor('n')

	# def south(self):
	# 	return self._neighbor('s')

	# def east(self):
	# 	return self._neighbor(east)

	# def west(self):
	# 	return self._neighbor('w')

	# def forward(self):
	# 	return self._neighbor('forward')

	# def back(self):
	# 	return self._neighbor('back')

	# def left(self):
	# 	return self._neighbor('left')

	# def right(self):
	# 	return self._neighbor('right')

	# def inspect(self):
	# 	return self._neighbor('inspect')

	# def intimidate(self):
	# 	return self._neighbor('intimidate')

	# def attack(self):
	# 	return self._neighbor('attack')

	# def talk(self):
	# 	return self._neighbor('talk')