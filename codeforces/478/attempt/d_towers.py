# with reverence, a port of http://codeforces.com/contest/478/submission/9123332

import fileinput, collections

###          ###
# utility func #
###          ###

dbug = True

def stoi(s):
	return([ int(x) for x in s.split() ])

def pd(s, label=''):
	global dbug
	if dbug:
		header = 'debug:'
		if label != '':
			header += ' (%s)\t' % label
		print header, s

###          ###
# code follows #
###          ###

MOD = 10 ** 9 + 7

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(stoi(args[0]))

def n_blocks(h):
	return h * (h + 1) / 2

def solve(args, verbose=False):
	global MOD
	(r, g) = proc_input(args)
	# CACHE[i] -> number of ways given i red blocks
	CACHE = collections.defaultdict(int)
	CACHE[0] = CACHE[1] = 1
	h = 2
	while(n_blocks(h) <= r + g):
		# minimum number of red blocks in the tower
		n_r = max(n_blocks(h) - g, 0)
		# calculate CACHE for all potential red blocks on this level
		for p_r in xrange(r, n_r - 1, -1):
			# we can add another level using p_r blocks to the tower
			if p_r >= h:
				CACHE[p_r] += CACHE[p_r - h]
			CACHE[p_r] %= MOD
		h += 1

	# undo the last increment option -- achieve the max height
	h -= 1
	acc = 0

	for n_r in xrange(max(n_blocks(h) - g, 0), r + 1):
		acc += CACHE[n_r]
		acc %= MOD
	if verbose:
		print acc
	return acc

def test():
	assert(solve([ '1 1' ]) == 2)
	assert(solve([ '4 6' ]) == 2)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
