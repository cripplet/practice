import fileinput, math

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
	(n, m) = proc_input(args)
	(a, b) = (math.ceil(float(n) / 2), n)
	between = math.ceil(a / m) * m
	r = between if between <= b else -1
	r = int(r)
	if verbose:
		print r
	return r

def test():
	assert(solve([ '10 2' ]) == 6)
	assert(solve([ '2 2' ]) == 2)
	assert(solve([ '29 7' ]) == 21)
	assert(solve([ '10000 2' ]) == 5000)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
