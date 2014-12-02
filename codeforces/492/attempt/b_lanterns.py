import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, l) = str_to_int(args[0])
	a = tuple(str_to_int(args[1]))
	return(l, a)

def solve(args, verbose=False):
	(l, a) = proc_input(args)
	list_a = list(a)
	list_a.sort()
	max_dist = max(list_a[0] * 2, (l - list_a[-1]) * 2)
	for x in xrange(len(a) - 1):
		max_dist = max(max_dist, list_a[x + 1] - list_a[x])
	if verbose:
		print max_dist / float(2)
	return max_dist / float(2)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(proc_input([ '2 5', '2 5' ]) == (5, (2, 5)))
	assert(solve([ '2 5', '2 5' ]) == 2.0)
	assert(solve([ '4 5', '0 1 2 3' ]) == 2.0)
	assert(solve([ '7 15', '15 5 3 7 9 14 0' ]) == 2.5)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
