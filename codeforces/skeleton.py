import fileinput

###          ###
# utility func #
###          ###

dbug = True

def stoi(s):
	return([ int(x) for x in s.split() ])

def pd(s):
	global dbug
	if dbug:
		print 'dbug: ', s

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return args

def solve(args, verbose=False):
	r = proc_input(args)
	if verbose:
		pass
	return None

def test():
	pass

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
