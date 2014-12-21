import fileinput

MOD = 10 ** 9 + 7

###          ###
# utility func #
###          ###

dbug = True

def stoi(s):
	return([ int(x) for x in s.split() ])

def pd(s):
	global dbug
	if dbug:
		print 'dbug: ', s

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(stoi(args[0]))

# n, x, b are 1-indexed
def floor_gen(n, x, b):
	d_above = d_below = abs(b - x) - 1
	l = range(max(x - d_below, 1), min(x + d_above, n) + 1)
	if x in l:
		l.remove(x)
	return(l)

def dp(n, a, b, k):
	# rows of k, cols of x
	CACHE = []
	FLOOR = [ floor_gen(n, x + 1, b) for x in xrange(n) ]
	for kp in xrange(k):
		CACHE.append([ None ] * n)
	# init, 0-indexed floors
	for x in xrange(n):
		CACHE[0][x] = len(floor_gen(n, x + 1, b))
	for kp in xrange(1, k):
		for x in range(n):
			CACHE[kp][x] = sum(CACHE[kp - 1][i - 1] for i in FLOOR[x])
	return CACHE[k - 1][a - 1]

def solve(args, verbose=False):
	(n, a, b, k) = proc_input(args)
	r = dp(n, a, b, k)
	if verbose:
		print r
	return r

def test():
	assert(floor_gen(10, 8, 10) == [ 7, 9 ])
	assert(solve([ '5 2 4 1' ]) == 2)
	assert(solve([ '5 4 2 1' ]) == 2)
	assert(solve([ '5 3 4 1' ]) == 0)
	assert(solve([ '2 2 1 1' ]) == 0)
	assert(solve([ '10 1 10 2' ]) == 44)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
