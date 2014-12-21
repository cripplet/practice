import fileinput

MOD = 10 ** 9 + 7

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

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(stoi(args[0]))

# n, x, b are 1-indexed
def floor_gen(n, x, b):
	d_above = d_below = abs(b - x) - 1
	l = range(max(x - d_below, 1), min(x + d_above, n) + 1)
	if x in l:
		l.remove(x)
	return(l)

def dp(n, a, b, k):
	# rows of k, cols of x
	CACHE = []
	FLOOR = [ floor_gen(n, x + 1, b) for x in xrange(n) ]
	for kp in xrange(k):
		CACHE.append([ None ] * n)
	# init, 0-indexed floors
	for x in xrange(n):
		CACHE[0][x] = len(floor_gen(n, x + 1, b))

	PARTIAL = [ 0 ] * n
	# passed in as 1-indexed
	def _ps(l, r):
		if l > r:
			result = 0
		else:
			assert(l > 0 and r > 0)
			# 0-indexed
			(l, r) = (l - 1, r - 1)
			(lv, rv) = (0, PARTIAL[r])
			if l > 0:
				lv = PARTIAL[l - 1]
			result = rv - lv
		return result

	for kp in xrange(1, k):
		# partial sum initialization
		s = 0
		for x in xrange(n):
			s += CACHE[kp - 1][x]
			PARTIAL[x] = s
		for x in xrange(n):
			# constant time lookup
			CACHE[kp][x] = 0
			if len(FLOOR[x]) > 0:
				CACHE[kp][x] = _ps(FLOOR[x][0], x) + _ps(x + 2, FLOOR[x][-1])
	return CACHE[k - 1][a - 1]

def solve(args, verbose=True):
	(n, a, b, k) = proc_input(args)
	r = dp(n, a, b, k)
	if verbose:
		print r
	return r

def test():
	assert(floor_gen(10, 8, 10) == [ 7, 9 ])
	assert(solve([ '5 2 4 1' ]) == 2)
	assert(solve([ '5 4 2 1' ]) == 2)
	assert(solve([ '5 2 4 2' ]) == 2)
	assert(solve([ '5 3 4 1' ]) == 0)
	assert(solve([ '2 2 1 1' ]) == 0)
	assert(solve([ '10 1 10 2' ], verbose=True) == 44)
	solve([ '2222 1206 1425 2222' ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
