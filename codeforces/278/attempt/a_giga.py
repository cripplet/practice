import fileinput

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(int(args[0]))

def solve(args, verbose=False):
	a = proc_input(args)
	b = 1
	while('8' not in list(str(a + b))):
		b += 1
	assert(b > 0)
	if verbose:
		print b
	return b

def test():
	assert(proc_input([ '179' ]) == 179)
	assert(solve([ '179' ]) == 1)
	assert(solve([ '-1' ]) == 9)
	assert(solve([ '18' ]) == 10)
	assert(solve([ '1000000000' ]) == 8)
	assert(solve([ '-1000000000' ]) == 2)
	assert(solve([ '0' ]) == 8)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
