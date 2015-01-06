import fileinput, math

###          ###
# utility func #
###          ###

dbug = True

def btos(b):
	return 'YES' if b else 'NO'

def pd(s, label=''):
	global dbug
	if dbug:
		header = 'debug:'
		if label != '':
			header += ' (%s)\t' % label
		print header, s

def stoi(s):
	return([ int(x) for x in s.split() ])

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
	if type(actual) != type([]):
		(actual, expected) = ([ actual ], [ expected ])
	if len(actual) != len(expected):
		return False
	r = [ expected[i] - tolerance <= actual[i] <= expected[i] + tolerance for i in xrange(len(actual)) ]
	return sum(r) == len(r)

def btod(b):
	return b * 2 - 1

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

def test_utilities():
	assert(stoi('1 2 3\n') == [ 1, 2, 3 ])
	assert(stoi('') == stoi('\n') == [])
	assert(perm(10, 5) == 30240)
	assert(comb(10, 5) == 252)
	assert(tol(0.0, 0.0) == tol(0.0, 0.1, tolerance=0.1) == tol(0.0, 10, tolerance=10) == True)
	assert(tol(0.0, 0.1) == tol(0.0, 0.1, tolerance=0.1 - 10 ** -9) == False)
	assert(tol([ 1.0, 1.1 ], [ 2.0, 2.1 ], tolerance=1) == True)
	assert(tol([ 1, 2 ], [ 1 ]) == tol([ 1 ], [ 1, 2 ]) == False)
	assert(_sigma(1) == 1)
	assert(_sigma(10) == 55)
	assert(sigma(1, 10) == 55)
	assert(sigma(3, 10) == 52)
	assert(sigma(10, 10) == 10)
	assert(sigma(10, 11) == 21)
	assert(ps([ 1 ]) == [ 1 ])
	assert(ps([ 1, 2, 3, 4, 5 ]) == [ 1, 3, 6, 10, 15 ])
	assert(btod(0) == -1)
	assert(btod(1) == 1)
	assert(btos(True) == 'YES')
	assert(btos(False) == 'NO')

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	n = int(args[0])
	d = [ stoi(l) for l in args[1:] ]
	return(n, d)

def solve(args, verbose=False):
	(n, d) = proc_input(args)

	# check this is undirected graph
	succ = True
	for i in xrange(n):
		succ &= (d[i][i] == 0)
		for j in xrange(i):
			succ &= (d[i][j] == d[j][i] and d[i][j] > 0)

	# given a tree T and nodes o, c, i such that
	#	1.) o is any node such that d(i, o) < inf
	#	2.) c is closest adjacent node to i (i.e. min[c](d(i, c)))
	# consider path P(i, o):
	#	case 1: if c in P: then we pass through c on the way from i to o
	#		o -- c -- i
	#	case 2: else: o is on the 'other side' of i than c
	#		o -- i -- c
	#	(here, -- designates actual edges)
	# case 1: d(o, i) == d(o, c) + d(c, i)
	# case 2: d(o, c) == d(o, i) + d(i, c)
	# algebra:
	#	case 1: d(i, c) == d(o, i) - d(o, c)
	#	case 2: d(i, c) == d(o, c) - d(o, i)
	# note that |d(i, c)| == |d(o, i) - d(o, c)|
	# we can use this property of trees to test for accurate edge weights
	#	1.) iterate among (i, o) pairs in O(n ** 2) complexity
	#	2.) for each (i, o) pair, find c of i
	#	3.) assert that for this (i, o) pair, the above property holds
	# credit to http://codeforces.com/contest/472/submission/9369316 and discussions with Kevin Wang
	for i in xrange(n):
		c = 0;
		# search for node closest c to node i -- cache this for this loop
		for o in xrange(n):
			if i == o:
				continue
			if d[i][o] < d[i][c]:
				c = o
		# test for property
		for o in xrange(n):
			succ &= abs(d[i][c]) == abs(d[o][i] - d[o][c])

	if verbose:
		print btos(succ)
	return succ

def test():
	assert(solve([ '3', '0 2 7', '2 0 9', '7 9 0' ], verbose=True) == True)
	assert(solve([ '3', '1 2 7', '2 0 9', '7 9 0' ]) == False)
	assert(solve([ '3', '0 2 2', '7 0 9', '7 9 0' ]) == False)
	assert(solve([ '3', '0 2 2', '7 0 9', '7 9 0' ]) == False)
	assert(solve([ '3', '0 1 1', '1 0 1', '1 1 0' ]) == False)
	assert(solve([ '2', '0 0', '0 0' ]) == False)
	assert(solve([ '1', '0' ]) == True)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
