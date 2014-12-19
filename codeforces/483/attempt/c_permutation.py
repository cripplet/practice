import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(str_to_int(args[0]))

def solve(args, verbose=False):
	(n, k) = proc_input(args)
	perm = [ 1 ] * n
	mult = 1
	ind = 1
	while ind != k + 1:
		perm[ind] = perm[ind - 1] + mult * (k - ind + 1)
		mult *= -1
		ind += 1

	for i in xrange(ind, n):
		perm[i] = i + 1

	if verbose:
		print ' '.join([ str(x) for x in perm ])
	return(perm)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '3 2' ]) == [ 1, 3, 2 ])
	assert(solve([ '5 2' ]) == [ 1, 3, 2, 4, 5 ])
	assert(solve([ '3 1' ]) == [ 1, 2, 3 ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
