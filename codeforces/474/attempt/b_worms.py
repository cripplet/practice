import fileinput, math

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

def perm(n, k, wheels=True):
	if wheels:
		assert(n > 0)
		assert(k > 0)
	return math.factorial(n) / math.factorial(k)

def comb(n, k, wheels=True):
	if wheels:
		assert(n > 0)
		assert(k > 0)
		assert(n - k > 0)
	return perm(n, k, False) / math.factorial(n - k)

def tol(actual, expected, tolerance=10 ** -9):
	return expected - tolerance <= actual <= expected + tolerance

def _sigma(f):
	return f * (f + 1) / 2

# sum(x from i to f)
def sigma(i, f, wheels=True):
	if wheels:
		assert(i >= 0)
		assert(f >= 0)
	return _sigma(f) - _sigma(i - 1)

def ps(l, wheels=True):
	if wheels:
		assert(len(l) > 0)
	r = [ l[0] ] * len(l)
	for i in xrange(1, len(l)):
		r[i] = l[i] + r[i - 1]
	return r

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(stoi(args[1]), stoi(args[3]))

def solve(args, verbose=False):
	(piles, worms) = proc_input(args)
	ps_piles = ps(piles)
	import bisect
	r = [ bisect.bisect_left(ps_piles, w) + 1 for w in worms ]
	if verbose:
		for p in r:
			print p
	return r

def test():
	assert(_sigma(10) == 55)
	assert(sigma(3, 10) == 52)
	assert(sigma(1, 1) == 1)
	assert(sigma(3, 4) == 7)
	assert(ps([ 1, 2, 3 ]) == [ 1, 3, 6 ])
	assert(solve([ '5', '2 7 3 4 9', '3', '1 25 11' ], verbose=True) == [ 1, 5, 3 ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
