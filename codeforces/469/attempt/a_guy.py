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
	n = int(args[0])
	p = stoi(args[1])[1:]
	q = stoi(args[2])[1:]
	return(n, p, q)

def solve(args, verbose=False):
	(n, p, q) = proc_input(args)
	pq = set(p + q)
	succ = len(pq) == n
	if verbose:
		print 'I become the guy.' if succ else 'Oh, my keyboard!'
	return succ

def test():
	assert(solve([ '4', '3 1 2 3', '2 2 4' ]) == True)
	assert(solve([ '4', '3 1 2 3', '2 2 3' ]) == False)
	assert(solve([ '100', '100 22 27 26 18 100 6 83 39 58 78 28 33 74 43 46 7 2 48 87 31 30 95 84 61 62 14 19 81 64 36 32 15 60 93 54 52 1 94 16 37 44 63 35 67 79 42 72 68 56 25 20 9 57 97 73 51 86 85 98 91 17 34 75 12 50 38 66 65 55 99 29 47 10 23 49 13 11 69 70 3 77 4 8 40 92 76 45 90 82 96 21 5 41 80 71 88 59 53 24 89', '100 22 27 26 18 100 6 83 39 58 78 28 33 74 43 46 7 2 48 87 31 30 95 84 61 62 14 19 81 64 36 32 15 60 93 54 52 1 94 16 37 44 63 35 67 79 42 72 68 56 25 20 9 57 97 73 51 86 85 98 91 17 34 75 12 50 38 66 65 55 99 29 47 10 23 49 13 11 69 70 3 77 4 8 40 92 76 45 90 82 96 21 5 41 80 71 88 59 53 24 89' ]) == True)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
