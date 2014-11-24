import fileinput
from math import ceil

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(hy, ay, dy) = [ int(x) for x in args[0].split() ]
	(hm, am, dm) = [ int(x) for x in args[1].split() ]
	(h, a, d) = [ int(x) for x in args[2].split() ]
	return(hy, ay, dy, hm, am, dm, h, a, d)

def to_win(ay, dy, hm, am, dm, verbose=0):
	dmgy = max(0, am - dy)
	dmgm = max(0, ay - dm)
	if dmgm == 0:
		return float('inf')
	if dmgy == 0:
		return 0
	nturns = ceil(float(hm) / dmgm)
	return (dmgy * nturns) + 1

def solve(args, verbose=False):
	(a, b, c, i, j, k, x, y, z) = proc_input(args)
	lookup = {}
	min = float('inf')
	for a_y in xrange(b, 200 + 1):
		for d_y in xrange(c, 100 + 1):
			r = (a_y - b) * y + (d_y - c) * z
			r += max(0, to_win(a_y, d_y, i, j, k) - a) * x
			if min > r:
				min = r
	assert(min >= 0)
	if verbose:
		print int(min)
	return int(min)
				

def test():
	assert(proc_input([ '1 2 3', '4 5 6', '7 8 9' ]) == (1, 2, 3, 4, 5, 6, 7, 8, 9))
	assert(solve([ '1 2 1', '1 100 1', '1 100 100' ]) == 99)
	assert(solve([ '100 100 100', '1 1 1', '1 1 1' ]) == 0)
	assert(solve([ '76 63 14', '89 87 35', '20 15 56' ]) == 915)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
