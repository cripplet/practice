import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	digits = list([ int(x) for x in args[0].strip() ])
	return digits

def solve(args, verbose=False):
	lookup = [ 2, 7, 2, 3, 3, 4, 2, 5, 1, 2 ]
	acc = 1
	for i in proc_input(args):
		acc *= lookup[i]
	if verbose:
		print acc
	return acc

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '89' ]) == 2)
	assert(solve([ '00' ]) == 4)
	assert(solve([ '73' ]) == 15)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
