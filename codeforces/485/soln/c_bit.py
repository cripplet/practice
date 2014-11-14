import fileinput

def high_order(x):
	return len(bin(x)) - 3

def proc((l, r)):
	b = high_order(r)
	cache = 1 << b
	if(cache <= l):
		return(proc((l - cache, r - cache)) + cache)
	if (cache << 1) - 1 <= r:
		# 2 ** (b + 1)
		return((cache << 1) - 1)
	else:
		# 2 ** b
		return(cache - 1)
	return ret

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	n = int(args[0])
	p = []
	for l in args[1:]:
		if l.split() != []:
			p.append(tuple( int(x) for x in l.split() ))
	return p

def solve(args, verbose=False):
	p = proc_input(args)
	r = []
	for e in p:
		r.append(proc(e))
	if verbose:
		for e in r:
			print e
	return r

stress = []
def test():
	assert(proc_input([ '3', '1 2', '2 3', '3 4' ]) == [ (1, 2), (2, 3), (3, 4) ])
	assert(high_order(1) == 0)
	assert(high_order(2) == 1)
	assert(high_order(4) == 2)
	assert(high_order(10) == 3)
	assert(proc((1, 2)) == 1)
	assert(proc((2, 4)) == 3)
	assert(proc((1, 10)) == 7)
	assert(proc((1, 3)) == 3)
	assert(solve([ '1', '1 3' ]) == [ 3 ])
	global stress
	(l, r) = ((1 << 18) - 2, (1 << 18) - 1)
	for x in xrange(10 ** 5):
		stress.append('%i %i' % (l, r))
	stress.insert(0, 10 ** 5)
	assert(len(stress) == 10 ** 5 + 1)
	from timeit import timeit
	assert(timeit('solve(stress)', setup='from __main__ import solve, stress', number=1))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
