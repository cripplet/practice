import fileinput, math, collections

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
	return(stoi(args[0]))

def solve(args, verbose=False):
	LOOKUP = { 2 : "Alien", 1 : "Elephant", 0 : "Bear" }
	sticks = sorted(proc_input(args))
	count = collections.defaultdict(int)
	for s in sticks:
		count[s] += 1
	r = 2
	for k, v in count.items():
		if v >= 4:
			for _ in xrange(4):
				sticks.pop(sticks.index(k))
			r = sticks[0] == sticks[1]
		
	if verbose:
		print LOOKUP[r]
	return r

def test():
	assert(solve([ '4 2 5 4 4 4' ]) == 0)
	assert(solve([ '4 4 5 4 4 5' ]) == 1)
	assert(solve([ '4 4 4 4 4 4' ]) == 1)
	assert(solve([ '1 2 3 4 5 6' ]) == 2)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
