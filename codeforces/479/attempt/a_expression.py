import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(a, b, c) = [ int(x) for x in args ]
	return(a, b, c)

def parse(a, b, c, mask):
	mult_first = mask & 1
	parn_first = (mask & 2) >> 1
	if mult_first:
		if parn_first:
			return (a * b) + c
		return a * (b + c)
	if parn_first:
		return (a + b) * c
	return a + (b * c)
	

def solve(args, verbose=False):
	(a, b, c) = proc_input(args)
	m = -float('inf')
	for i in xrange(4):
		m = max(m, parse(a, b, c, i))
	m = max(m, a * b * c)
	m = max(m, a + b + c)
	if verbose:
		print m
	return m

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '1', '2', '3' ]) == 9)
	assert(solve([ '2', '10', '3' ]) == 60)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
