import fileinput

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	pass

def solve(args, verbose=False):
	r = proc_input(args)

def test():
	pass

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve([ l for l in fileinput.input() ], verbose=True)
