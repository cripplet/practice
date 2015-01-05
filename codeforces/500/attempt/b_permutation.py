import fileinput, math

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

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	p = stoi(args[1])
	m = [ args[2 + i].strip() for i in xrange(len(p)) ]
	return(p, m)

def solve(args, verbose=False):
	from Queue import Queue as Q
	(p, m) = proc_input(args)
	# http://stackoverflow.com/a/8124880/873865
	comp_id = -1
	scratch = [ -1 ] * len(p)
	for n in xrange(len(p)):
		comp_id += 1
		q = Q()
		q.put(n)
		while not q.empty():
			node = q.get()
			# already processed
			if scratch[node] != -1:
				continue
			scratch[node] = comp_id
			for k, v in enumerate(m[node]):
				if v == '1':
					q.put(k)
	components = [ [] for _ in xrange(len(p)) ]
	for ind, comp in enumerate(scratch):
		components[comp].append((p[ind], ind))

	res = [ 0 ] * len(p)
	for c in components:
		if c == []:
			continue
		(v, k) = [ list(x) for x in zip(*c) ]
		v.sort()
		k.sort()
		for ind, val in enumerate(v):
			res[k[ind]] = val

	if verbose:
		print ' '.join([ str(x) for x in res ])
	return res

def test():
	assert(solve([ '7', '5 2 4 3 6 7 1', '0001001', '0000000', '0000010', '1000001', '0000000', '0010000', '1001000' ], verbose=True) == [ 1, 2, 4, 3, 6, 7, 5 ])
	assert(solve([ '5', '4 2 1 5 3', '00100', '00011', '10010', '01101', '01010' ], verbose=True) == [ 1, 2, 3, 4, 5 ])


if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
