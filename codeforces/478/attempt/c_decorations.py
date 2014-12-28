import fileinput

###          ###
# utility func #
###          ###

dbug = True

def stoi(s):
	return([ int(x) for x in s.split() ])

def pd(s, label=''):
	global dbug
	if dbug:
		header = 'debug:'
		if label != '':
			header += ' (%s)\t' % label
		print header, s

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(stoi(args[0]))

def solve(args, verbose=False):
	balloons = sorted(proc_input(args))
	r = sum(balloons) / 3
	if balloons[-1] / 2 >= sum(balloons[:2]):
		r = sum(balloons[:2])
	if verbose:
		print r
	return r

def test():
	assert(solve([ '5 4 3' ]) == 4)
	assert(solve([ '1 1 1' ]) == 1)
	assert(solve([ '2 3 3' ]) == 2)
	assert(solve([ '4 0 4' ]) == 2)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
