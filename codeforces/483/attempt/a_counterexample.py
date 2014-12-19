import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(l, r) = str_to_int(args[0])
	return(l, r)

def solve(args, verbose=False):
	(l, r) = proc_input(args)
	t = l
	while t % 2:
		t += 1
	res = (t, t + 1, t + 2)
	if t + 2 > r:
		res = (-1,)
	if verbose:
		for x in res:
			print x
	return(res)
		

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
