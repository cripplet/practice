import fileinput, math, itertools

###          ###
# utility func #
###          ###

dbug = True

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

def test_utilities():
	assert(stoi('1 2 3\n') == [ 1, 2, 3 ])
	assert(stoi('') == stoi('\n') == [])
	assert(perm(10, 5) == 30240)
	assert(comb(10, 5) == 252)
	assert(tol(0.0, 0.0) == tol(0.0, 0.1, tolerance=0.1) == tol(0.0, 10, tolerance=10) == True)
	assert(tol(0.0, 0.1) == tol(0.0, 0.1, tolerance=0.1 - 10 ** -9) == False)
	assert(_sigma(1) == 1)
	assert(_sigma(10) == 55)
	assert(sigma(1, 10) == 55)
	assert(sigma(3, 10) == 52)
	assert(sigma(10, 10) == 10)
	assert(sigma(10, 11) == 21)
	assert(ps([ 1 ]) == [ 1 ])
	assert(ps([ 1, 2, 3, 4, 5 ]) == [ 1, 3, 6, 10, 15 ])

def btod(b):
	return 2 * b - 1

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	n = int(args[0])
	regiments = []
	for i in xrange(n):
		regiments.append([ stoi(args[1 + (4 * i) + j]) for j in xrange(4) ])
	return regiments

def dist((a, b), (x, y)):
	return (x - a) ** 2 + (y - b) ** 2

def is_sq(coord):
	for (a, b, c, d) in itertools.permutations(coord):
		_sq = True
		_sq &= dist(a, b) == dist(b, c) == dist(c, d) == dist(d, a)
		_sq &= dist(a, c) == dist(b, d)
		_sq &= ((dist(a, b) + dist(b, c)) == dist(a, c) and dist(a, b) != dist(a, c))
		if _sq:
			break
	return _sq

def dir(d):
	return (btod((d & 2) >> 1), btod(d & 1))

def generate((x, y, a, b), d):
	(dx, dy) = dir(d)
	(_x, _y) = (x - a, y - b)
	if dx * dy == 1:
		(_x, _y) = (_x * dx, _y * dy)
	else:
		(_x, _y) = (_y * dy, _x * dx)
	return(_x + a, _y + b)

def solve(args, verbose=False):
	regiments = proc_input(args)
	rs = []
	for k, r in enumerate(regiments):
		_r = float('inf')
		for p in xrange(4 ** 4):
			masks = [ (p & (3 << (2 * i))) >> (2 * i) for i in xrange(4) ]
			coord = [ generate(r[i], masks[i]) for i in xrange(4) ]
			if is_sq(coord):
				_r = min(_r, sum([ dir(x).count(-1) for x in masks ]))
		if _r == float('inf'):
			_r = -1
		rs.append(_r)
	if verbose:
		for r in rs:
			print r
	return rs

def test():
	assert(is_sq(((0, 0), (0, 1), (1, 0), (1, 1))) == True)
	assert(generate((100, 1, 0, 0), 0) == (-100, -1))
	assert(generate((100, 1, 0, 0), 1) == (1, -100))
	assert(generate((100, 1, 0, 0), 2) == (-1, 100))
	assert(generate((100, 1, 0, 0), 3) == (100, 1))
	assert(solve([ '1', '1 1 0 0', '-1 1 0 0', '-1 1 0 0', '1 -1 0 0' ]) == [ 1 ])
	assert(solve([ '1', '1 1 0 0', '-2 1 0 0', '-1 1 0 0', '1 -1 0 0' ]) == [ -1 ])
	assert(solve([ '1', '1 1 0 0', '-1 1 0 0', '-1 1 0 0', '-1 1 0 0' ]) == [ 3 ])
	assert(solve([ '1', '2 2 0 1', '-1 0 0 -2', '3 0 0 -2', '-1 1 -2 0' ]) == [ 3 ])
	assert(solve([ '2', '1 1 0 0', '-1 1 0 0', '-1 1 0 0', '1 -1 0 0', '1 1 0 0', '-2 1 0 0', '-1 1 0 0', '1 -1 0 0' ]) == [ 1, -1 ])
	assert(solve([ '1', '-2248 6528 -2144 6181', '-2245 6663 -2100 7054', '-4378 7068 -4061 7516', '-4274 6026 -3918 5721' ], verbose=True) == [ 8 ])


if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
