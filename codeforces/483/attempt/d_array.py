import fileinput, sys

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, m) = str_to_int(args[0])
	constraints = []
	for i in xrange(m):
		constraints.append(str_to_int(args[i + 1]))
	return(n, m, constraints)

def solve(args, verbose=False):
	(n, m, constraints) = proc_input(args)
	out = [ 0 ] * n
	for (l, r, q) in constraints:
		for i in xrange(l - 1, r):
			out[i] |= q
	verify = True
	for (l, r, q) in constraints:
		result = sys.maxint
		for i in xrange(l - 1, r):
			result &= out[i]
		if result != q:
			verify = False
			out = []
			break
	if verbose:
		if verify:
			print 'YES'
			print ' '.join([ str(x) for x in out ])
		else:
			print 'NO'
	return(verify, out)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(proc_input([ '3 1', '1 3 3' ]) == (3, 1, [ [ 1, 3, 3 ] ]))
	assert(solve([ '3 1', '1 3 3' ]) == (True, [ 3, 3, 3 ]))
	assert(solve([ '3 2', '1 3 3', '1 3 2' ]) == (False, []))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
