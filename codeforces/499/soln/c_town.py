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
	(hx, hy) = stoi(args[0])
	(ux, uy) = stoi(args[1])
	lines = []
	for l in args[3:]:
		lines.append(stoi(l))
	return(hx, hy, ux, uy, lines)

def solve(args, verbose=False):
	(hx, hy, ux, uy, lines) = proc_input(args)
	r = sum([ (a * hx + b * hy + c > 0) ^ (a * ux + b * uy + c > 0) for (a, b, c) in lines ])
	if verbose:
		print r
	return r

def test():
	assert(solve([ '1 1', '-1 -1', '2', '0 1 0', '1 0 0' ]) == 2)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
