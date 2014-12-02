import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return int(args[0])

def solve(args, verbose=False):
	n = proc_input(args)
	n_used = 0
	steps = 1
	count = 1
	while n >= count:
		n -= count
		steps += 1
		count += steps
	if verbose:
		print steps - 1
	return steps - 1

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '1' ]) == 1)
	assert(solve([ '25' ]) == 4)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
