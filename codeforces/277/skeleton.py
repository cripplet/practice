import fileinput

def solve(args, verbose=False):
	pass

def test():
	pass

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(fileinput.input(), verbose=True)
