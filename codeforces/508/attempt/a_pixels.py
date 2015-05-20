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
	(n, m, k) = stoi(args[0])
	coord = [ stoi(l) for l in args[1:] ]
	assert(len(coord) == k)
	return n, m, k, coord

def solve(args, verbose=False):
	(r, c, k, coord) = proc_input(args)
	m = [ [ 0 for _ in xrange(c + 2) ] for _ in xrange(r + 2) ]
	res = 0
	for k, (_r, _c) in enumerate(coord):
		m[_r][_c] = 1
		if m[_r - 1][_c - 1] + m[_r - 1][_c] + m[_r][_c - 1] == 3 or \
			m[_r - 1][_c] + m[_r - 1][_c + 1] + m[_r][_c + 1] == 3 or \
			m[_r][_c - 1] + m[_r + 1][_c - 1] + m[_r + 1][_c] == 3 or \
			m[_r][_c + 1] + m[_r + 1][_c] + m[_r + 1][_c + 1] == 3:
			res = k + 1
			break
	if verbose:
		print res
	return res

def test():
	assert(solve([ '2 2 4', '1 1', '1 2', '2 1', '2 2' ], verbose=True) == 4)
	assert(solve([ '2 3 6', '2 3', '2 2', '1 3', '2 2', '1 2', '1 1' ], verbose=True) == 5)
	assert(solve([ '5 3 7', '2 3', '1 2', '1 1', '4 1', '3 1', '5 3', '3 2' ], verbose=True) == 0)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)