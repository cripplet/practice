import fileinput

def proc_input(args=[]):
	m = 0
	n = 0
	b = []
	size_known = False
	for l in args:
		if not size_known:
			size_known = True
			(m, n) = [ int(x) for x in l.split() ]
		else:
			b.append([ int(x) for x in l.split() ])
	return(m, n, b)

def gen(prefix, m, n, s):
	t = [ [ (prefix + 1) & 1 for c in xrange(n) ] for r in xrange(m) ]
	for r in xrange(m):
		for c in xrange(n):
			if s[r][c] == prefix:
				t[r] = [ prefix for _c in xrange(n) ]
				for _r in xrange(m):
					t[_r][c] = prefix
	return t

def gen_a(m, n, b):
	return gen(0, m, n, b)

def gen_b(m, n, a):
	return gen(1, m, n, a)

def solve(args, verbose=False):
	(m, n, b) = proc_input(args)
	a = gen_a(m, n, b)
	if(gen_b(m, n, a) == b):
		(r_v, r_a) = (True, a)
	else:
		(r_v, r_a) = (False, [])

	if(verbose):
		if not r_v:
			print 'NO'
		else:
			print 'YES'
			print '\n'.join([ ' '.join([ str(c) for c in r ]) for r in a ])
	return((r_v, r_a))

def test():
	assert(proc_input([ '1 1', '0' ]) == (1, 1, [ [ 0 ] ]))
	assert(proc_input([ '2 1', '1 0' ]) == (2, 1, [ [ 1, 0 ] ]))
	assert(gen_a(1, 1, [ [ 0 ] ]) == [ [ 0 ] ])
	assert(gen_a(1, 1, [ [ 1 ] ]) == [ [ 1 ] ])
	assert(gen_a(2, 2, [ [ 1, 0 ], [ 0, 0 ] ]) == [ [ 0, 0 ], [ 0, 0 ] ])
	assert(gen_b(2, 2, [ [ 0, 0 ], [ 0, 0 ] ]) == [ [ 0, 0 ], [ 0, 0 ] ])
	assert(solve([ '2 2', '1 0', '0 0' ]) == (False, []))
	assert(solve([ '2 3', '1 1 1', '1 1 1' ]) == (True, [ [ 1, 1, 1 ], [ 1, 1, 1 ] ]))
	assert(solve([ '2 3', '0 1 0', '1 1 1' ]) == (True, [ [ 0, 0, 0 ], [ 0, 1, 0 ] ]))

if __name__ == '__main__':
	from sys import argv
	if(argv.pop() == 'test'):
		test()
	else:
		solve(fileinput.input(), verbose=True)
