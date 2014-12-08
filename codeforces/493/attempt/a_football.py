import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

class Player(object):
	def __init__(self, team, id):
		self.team = team
		self.id = id
		self.first_red = None
		self.y = False
	def foul(self, time, type):
		if not self.first_red:
			if type == 'r':
				self.first_red = time
			else:
				if self.y:
					self.first_red = time
				else:
					self.y = True
	def get_foul(self):
		return self.first_red
					

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	home = args[0].strip()
	away = args[1].strip()
	n = int(args[2])
	players = []
	for l in args[3:]:
		x = l.split()
		players.append((int(x[0]), x[1], int(x[2]), x[3]))
	return (home, away, tuple(players))

def solve(args, verbose=False):
	(h, a, p) = proc_input(args)
	results = []
	players = {}
	for x in p:
		i = Player(x[1], x[2])
		if (i.team, i.id) not in players:
			players[(i.team, i.id)] = i
		players[(i.team, i.id)].foul(x[0], x[3])
	for k, v in players.items():
		if v.get_foul():
			team = h
			if v.team == 'a':
				team = a
			results.append((team, v.id, v.get_foul()))
	results.sort(key=lambda x: x[2])
	if verbose:
		for x in results:
			print x[0], x[1], x[2]
	return results

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ 'MC', 'CSKA', '9', '28 a 3 y', '62 h 25 y', '66 h 42 y', '70 h 25 y', '77 a 4 y', '79 a 25 y', '82 h 42 r', '89 h 16 y', '90 a 13 r']) == [ ('MC', 25, 70), ('MC', 42, 82), ('CSKA', 13, 90) ])
	assert(solve([ 'MASFF', 'SAFBDSRG', '5', '1 h 1 y', '15 h 1 r', '27 a 1 y', '58 a 1 y', '69 h 10 y' ]) == [ ('MASFF', 1, 15), ('SAFBDSRG', 1, 58) ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
