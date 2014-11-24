import fileinput
from math import ceil

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(hp_y, atk_y, def_y) = tuple([ int(x) for x in args[0].split() ])
	(hp_m, atk_m, def_m) = tuple([ int(x) for x in args[1].split() ])
	(h, a, d) = tuple([ int(x) for x in args[2].split() ])
	return(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d)

def is_win(hp_y, hp_m, dmg_y, dmg_m):
	if dmg_y == 0:
		return False
	if dmg_m == 0:
		return True
	n_turns = ceil(hp_m / float(dmg_y))
	r = (hp_m - (dmg_y * n_turns) <= 0) and (hp_y - (dmg_m * n_turns) > 0)
	return r

# key is (hp_y, atk_y, def_y), value is bitcoins
CACHE = {}
global_min = float('inf')

def dp_aux(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d, o_h, o_a, o_d):
	global CACHE, global_min
	k = (hp_y, atk_y, def_y)
	if k in CACHE:
		return CACHE[k]

	CACHE[k] = (hp_y - o_h) * h + (atk_y - o_a) * a + (def_y - o_d) * d

	dmg_y = max(0, atk_y - def_m)
	dmg_m = max(0, atk_m - def_y)
	if(not is_win(hp_y, hp_m, dmg_y, dmg_m)):
		if CACHE[k] > global_min:
			CACHE[k] = global_min
		else:
			c_h = dp_aux(hp_y + 1, atk_y, def_y, hp_m, atk_m, def_m, h, a, d, o_h, o_a, o_d) + h
			c_a = dp_aux(hp_y, atk_y + 1, def_y, hp_m, atk_m, def_m, h, a, d, o_h, o_a, o_d) + a
			c_d = dp_aux(hp_y, atk_y, def_y + 1, hp_m, atk_m, def_m, h, a, d, o_h, o_a, o_d) + d
			CACHE[k] = min(c_h, c_a, c_d)
	if CACHE[k] < global_min:
		global_min = CACHE[k]
	return CACHE[k]

def dp(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d):
	global CACHE, global_min
	CACHE = {}
	global_min = float('inf')
	dp_aux(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d, hp_y, atk_y, def_y)
	return global_min


def solve(args, verbose=False):
	(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d) = proc_input(args)
	r = dp(hp_y, atk_y, def_y, hp_m, atk_m, def_m, h, a, d)
	if verbose:
		print r
	return r
	
	

def test():
	assert(proc_input([ '1 2 3', '4 5 6', '7 8 9' ]) == (1, 2, 3, 4, 5, 6, 7, 8, 9))
	assert(is_win(10, 10, 2, 1) == True)
	assert(is_win(10, 10, 1, 2) == False)
	assert(dp(1, 2, 1, 1, 100, 1, 1, 100, 100) == 99)
	assert(dp(100, 100, 100, 1, 1, 1, 1, 1, 1) == 0)
	assert(dp(72, 16, 49, 5, 21, 84, 48, 51, 88))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
