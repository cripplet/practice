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

class ConnectedComponent(object):
	def __init__(self, v=None, k=None):
		self.vs = []
		self.ks = []
		if v is not None:
			self.iv(v)
		if k is not None:
			self.ik(k)

	def find(self, k):
		return k in self.ks

	def iv(self, v):
		if len(self.vs) == 0 or self.vs[0] < v:
			self.vs.append(v)
		else:
			self.vs.insert(0, v)

	def ik(self, k):
		self.ks.append(k)

	def __str__(self):
		return '%s, %s' % (str(self.vs), str(self.ks))

	def __add__(self, other):
		c = ConnectedComponent()
		for v in self.vs + other.vs:
			c.iv(v)
		for k in self.ks + other.ks:
			c.ik(k)
		return c

def solve(args, verbose=False):
	(p, m) = proc_input(args)
	components = [ ConnectedComponent(v, k) for (k, v) in enumerate(p) ]
	edges = []
	for i in xrange(len(m)):
		for j in xrange(i):
			if m[i][j] == '1':
				edges.append((i, j))
	for (s, t) in edges:
		for k, c in enumerate(components):
			if c.find(s):
				i = k
			if c.find(t):
				j = k
		if i != j:
			components[i] += components[j]
			components.pop(j)

	ans = [ 0 for _ in xrange(len(p)) ]
	for c in components:
		c.vs.sort()
		c.ks.sort()
		for i in xrange(len(c.vs)):
			ans[c.ks[i]] = c.vs[i]
	if verbose:
		print ' '.join(str(x) for x in ans)
	return ans

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
