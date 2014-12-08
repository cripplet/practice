import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, k) = str_to_int(args[0])
	data = str_to_int(args[1])
	return(k, data)

def solve(args, verbose=False):
	(k, data) = proc_input(args)
	agg = []
	dir = []
	for i in xrange(len(data) - 1):
		t = data[i - 1] - data[i]
		if t >
		

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
