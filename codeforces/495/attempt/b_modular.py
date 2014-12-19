import fileinput, math

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(a, b) = str_to_int(args[0])
	return(a, b)

def solve(args, verbose=False):
	(a, b) = proc_input(args)
	init = a - b
	r = 0
	x = 1
	if init:
		while x ** 2 <= init:
			if init % x == 0:
				if x > b:
					r += 1
				if init / x != x and init / x > b:
					r += 1
			x += 1
	else:
		r = 'infinity'
	if verbose:
		print r
	return r

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '21 5' ]) == 2)
	assert(solve([ '9435152 272']) == 282)
	assert(solve([ '10 10' ]) == 'infinity')
	assert(solve([ '0 1000000000' ]) == 0)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
