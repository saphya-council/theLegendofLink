import cmd
from room import get_room
#from player import player_equip
from player import *
from musescore_midi import *
import textwrap
import winsound

class Game(cmd.Cmd):
	#initializes the game
	def __init__(self):
		cmd.Cmd.__init__(self)
		#to play the music
		winsound.PlaySound("../zelda_intro.wav",  winsound.SND_ASYNC | winsound.SND_LOOP)
		asciiart = []
		asciiart = ["       __________",
		"       \        /    T  H  E    L  E  G  E  N  D    O  F",
		"        \      /     ___________      __________    _____",
		"        /     /      \     /\   \     |    /\  |   /    /",
		"       /     /        |   |  ||\ \    |   |  | |  /    /",
		"      /     /         |   |  || \ \   |   |  | | /    /",
		"     /     /          |   |  ||  \ \  |   |  | |/    /",
		"    /     /           |   |  ||   \ \ |   |  |      <",
		"   /     /            |   |  ||    \ \|   |  | |\     \\",
		"  /     /             |   |  ||     \     |  | | \     \\",
		" /     /_____________/_____\/_|      \_____\/__|  \_____\\",
		"/____________________/    AN  INTERACTIVE  FANFICTION"]

		for i in asciiart:
		    print ("\t"+ i)
		print("")
		print("")
		print("")
		print("")

		self.loc = get_room(1)
		self.look()
	#crosschecks input with location neighbors
	def move(self, dir):

		#global hint_count
		#dir = dir.lower()
		#print("direction to go: " + dir)
		newroom = self.loc._neighbor(dir)

		if newroom is None:
			if hints['hint'] == 3:
				print("Type (help) to open your command list and (m) to open the map.")
				hints['hint'] = 0
			else:
				print("You can't do that.")
				hints['hint']+=1

		else:
			# newroom = newroom.lower()
			self.loc = get_room(newroom)
			self.look()
			#update inventory
			if self.loc.equipped != '':
				player_equip["equipped"] = self.loc.equipped
			if self.loc.swords != '':
				player_equip["sword"] = self.loc.swords
			if self.loc.shields != '':
				player_equip["shield"] = self.loc.shields

			if self.loc.name == "Village - Market":
				area["merchant_visited"] = "1"

			if self.loc.name == "Forest - Entrance":
				area["forest_visited"] = "1"

	#prints location name and description
	def look(self):
		print(self.loc.name)
		print("")
		for line in textwrap.wrap(self.loc.description,72):
			print(line)

	def do_n(self, args):
		#print(args)
		"""Go north"""
		self.move('n')

	def do_s(self, args):
		"""Go south"""
		self.move('s')

	def do_e(self, args):
		"""Go east"""
		self.move('e')

	def do_w(self, args):
		"""Go west"""
		self.move('w')

	def do_forward(self, args):
		"""Go forward"""
		self.move('forward')

	def do_back(self, args):
		"""Go back"""
		self.move('back')

	def do_left(self, args):
		"""Go left"""
		self.move('left')

	def do_right(self, args):
		"""Go right"""
		self.move('right')

	def do_inspect(self, args):
		"""Inspect"""
		self.move('inspect')

	def do_intimidate(self, args):
		"""Intimidate"""
		self.move('intimidate')

	def do_attack(self, args):
		"""Attack"""
		self.move('attack')

	def do_talk(self, args):
		"""Talk"""
		self.move('talk')

	def do_i(self,args):
		"""Inventory"""
		inventory = player_equip.values()
		for i in inventory:
			print(i)
	
	def do_m(self,args):
		"""Map"""
		m = []
		m = ['                                      ___________     __________',
		'                                     |           |   |          |',
		'                                     |PLAYGROUND |   |  MARKET  |',
		'                                     |___________|   |__________|',
		'                                              |     /',
		' _________     _________     ________     ____|___ /   _________',
		'|         |   |         |   |        |   |        |   |         |',
		'| DUNGEON |---|MOUNTAINS|---| VALLEY |---|VILLAGE |---|  ALLEY  |',
		'|_________|   |_________|   |________|   |________|   |_________|', 
		'                                |             |',
		'                                |         ____|___',
		'                                |        |        |',
		'                                |        | FOREST |',
		'                                |        |________|',
		'         N                      |             |',
		'         |                   ___|____     ____|___',
		'     W---*---E              |        |   |        |',
		'         |                  |  LAKE  |<--|  CAVE  |',
		'         S                  |________|   |________|']

		for i in m:
		    print (i)


	def do_quit(self, args):
		"""Leaves the game"""
		print("Thank you for playing")
		#print(len(new_song))
		
		for i in new_song:
			print(i)

		new_song.show('midi')
		#new_song.show('new_song.png')

		#print(area["merchant_visited"])
		return True

if __name__ == "__main__":
	g = Game()
	g.cmdloop()

