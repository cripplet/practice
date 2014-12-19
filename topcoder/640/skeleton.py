import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	pass

def solve(args, verbose=False):
	r = proc_input(args)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
