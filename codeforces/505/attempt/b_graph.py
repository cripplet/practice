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
	(n, m) = stoi(args[0])
	e = [ stoi(l) for l in args[1:1 + m] ]
	q = [ stoi(l) for l in args[2 + m:] ]
	return (n, m, e, q)

adj_list = collections.defaultdict(lambda : collections.defaultdict(list))

def bfs((u, v)):
	global adj_list
	c = set(adj_list[u].keys())
	n_succ = 0
	for cp in c:
		q = collections.deque([ u ])
		is_visited = collections.defaultdict(int)
		while len(q):
			n = q.popleft()
			if is_visited[n] == len(adj_list[n][cp]):
				continue
			if n == v:
				n_succ += (n == v)
				break
			is_visited[n] += 1
			for b in adj_list[n][cp]:
				q.append(b)
	return n_succ

def solve(args, verbose=False):
	(n, m, e, q) = proc_input(args)
	global adj_list
	adj_list = collections.defaultdict(lambda : collections.defaultdict(list))
	for (a, b, c) in e:
		adj_list[a - 1][c].append(b - 1)
		adj_list[b - 1][c].append(a - 1)
	log = []
	for (u, v) in q:
		log.append(bfs((u - 1, v - 1)))
	if verbose:
		for i in log:
			print i
	return log

def test():
	assert(solve([ '4 5', '1 2 1', '1 2 2', '2 3 1', '2 3 3', '2 4 3', '3', '1 2', '3 4', '1 4' ], verbose=True) == [ 2, 1, 0 ])
	assert(solve([ '5 7', '1 5 1', '2 5 1', '3 5 1', '4 5 1', '1 2 2', '2 3 2', '3 4 2', '5', '1 5', '5 1', '2 5', '1 5', '1 4' ], verbose=True) == [ 1, 1, 1, 1, 2 ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
