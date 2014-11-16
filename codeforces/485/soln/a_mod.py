import fileinput

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(tuple([ int(x) for x in args[0].split() ]))

def proc(a, m):
	for i in xrange(33):
		if a * (1 << i) % m == 0:
			return True
	return False

def solve(args, verbose=False):
	(a, m) = proc_input(args)
	r = proc(a, m)
	if verbose:
		if r:
			print 'Yes'
		else:
			print 'No'
	return r

def test():
	assert(proc_input([ '1 2' ]) == (1, 2))
	assert(proc(1, 5) == False)
	assert(proc(3, 6) == True)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
