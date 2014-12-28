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
	end = proc_input(args)
	avg = sum(end) / len(end)
	r = -1
	if sum(end) % len(end) == 0 and sum(end) > 0:
		r = avg
	if verbose:
		print(r)
	return r

def test():
	assert(solve([ '2 5 4 0 4' ]) == 3)
	assert(solve([ '4 5 9 2 1' ]) == -1)
	assert(solve([ '0 0 0 0 0' ]) == -1)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
