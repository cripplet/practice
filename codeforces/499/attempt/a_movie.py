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
	(n, x) = stoi(args[0])
	times = []
	for l in args[1:]:
		times.append(stoi(l))
	return(n, x, times)

def solve(args, verbose=False):
	(n, x, times) = proc_input(args)
	times.sort(key=lambda(a, b): a)
	cur_t = 1
	ela_t = 0
	for (a, b) in times:
		ela_t += b - a + 1
		ela_t += (a - cur_t) % x
		cur_t = b + 1

	if verbose:
		print ela_t
	return ela_t

def test():
	assert(solve([ '2 3', '5 6', '10 12' ]) == 6)
	assert(solve([ '1 1', '1 100000']) == 100000)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
