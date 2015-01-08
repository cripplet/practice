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
	(_, a, b) = stoi(args[0])
	return(a, b, stoi(args[1]))

def solve(args, verbose=False):
	(a, b, p) = proc_input(args)
	partition = [ 1 ] * len(p)
	(_a, _b, p) = (set(), set(), { v : k for (k, v) in enumerate(p) })
	succ = True

	while len(p):
		(k, e) = (p[p.keys()[0]], p.keys()[0])
		p.pop(e)
		(ca, cb) = (a - e, b - e)
		if ca in _a or ca in p or e == ca:
			_a.add(e)
			partition[k] = 0
		elif cb in _b or cb in p or e == cb:
			_b.add(e)
			partition[k] = 1
		else:
			print 'false'
			print e, ca, cb, _a, _b, p
			succ = False
			break
	if verbose:
		print btos(succ)
		if succ:
			print ' '.join([ str(x) for x in partition ])
	if succ:
		return succ, partition
	return False

def test():
	assert(solve([ '4 5 9', '2 3 4 5' ]) == (True, [ 0, 0, 1, 1 ]))
	assert(solve([ '3 3 4', '1 2 4' ]) == False)
	assert(solve([ '1 10 100', '5' ]) == (True, [ 0 ]))
	assert(solve([ '70 416035 416023', '70034 70322 345689 345965 345701 70046 345737 345713 70166 345821 70010 345749 345677 345725 69962 345869 70178 70310 345785 69998 70070 69974 70058 346001 70106 345953 70226 70154 345929 69950 70298 346049 70346 345989 70286 69986 345893 70082 70238 345797 70250 345833 70334 345845 70094 70118 70202 345977 70262 70274 70190 345941 346025 345761 345773 70142 70022 70130 345881 345917 70358 345905 345665 346013 346061 345809 345857 346037 346073 70214' ], verbose=True) == (True, [ 1 ] * 70))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
