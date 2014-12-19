import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	a_s = tuple(str_to_int(args[1]))
	return(a_s)

def solve(args, verbose=False):
	a_s = proc_input(args)
	max_1 = -float('inf')
	min_2 = float('inf')
	# min_1
	for k in xrange(len(a_s) - 1):
		max_1 = max(max_1, a_s[k + 1] - a_s[k])
	for k in xrange(len(a_s) - 2):
		min_2 = min(min_2, a_s[k + 2] - a_s[k])
	r = max(max_1, min_2)
	if verbose:
		print r
	return r

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '3', '1 4 6' ]) == 5)
	assert(solve([ '5', '1 2 3 4 5' ]) == 2)
	assert(solve([ '5', '1 2 3 7 8' ]) == 4)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
