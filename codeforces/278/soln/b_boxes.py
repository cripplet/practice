import fileinput

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	n = int(args[0])
	l = tuple([ int(x) for x in args[1:1 + n] ])
	return l

CACHE = {}
def pre_proc():
	global CACHE
	for x in xrange(1, 501):
		for y in xrange(x, 3 * x + 1):
			CACHE[(x, y, 4 * x - y, 3 * x)] = True

def solve(args, verbose=False):
	global CACHE
	l = list(proc_input(args))
	s = None
	pre_proc()
	for k in CACHE:
		succ = True
		# check k is a superset of l
		for t in l:
			if k.count(t) < l.count(t):
				succ = False
		if succ:
			working = list(k)
			for t in k:
				if t in l:
					l.remove(t)
					working.remove(t)
			s = [ x for x in working if x not in l ]
			break
	if s == None:
		if verbose:
			print 'NO'
		return False
	if verbose:
		print 'YES'
		for x in s:
			print x
	return (True, tuple(s))

def test():
	assert(proc_input([ '2', '3', '4' ]) == (3, 4))
	assert(solve([ '2', '1', '1' ]) == (True, (3, 3)))
	assert(solve([ '3', '1', '1', '1' ]) == False)
	assert(solve([ '3', '1', '1', '3' ]) == (True, (3,)))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
