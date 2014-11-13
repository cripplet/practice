import fileinput

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	n = int(args[0])
	l = []
	for i in xrange(n):
		l.append(tuple([ int(x) for x in args[i + 1].split() ]))
	return(n, l)

def proc(l):
	xmin = ymin = float('inf')
	xmax = ymax = -float('inf')
	for (x, y) in l:
		xmin = min(xmin, x)
		xmax = max(xmax, x)
		ymin = min(ymin, y)
		ymax = max(ymax, y)
	return(max(ymax - ymin, xmax - xmin))

def solve(args, verbose=False):
	(n, l) = proc_input(args)
	r = proc(l) ** 2
	if verbose:
		print r
	return r

def test():
	assert(proc_input([ '3', '1 1', '2 2', '3 3' ]) == (3, [ (1, 1), (2, 2), (3, 3) ]))
	assert(proc([ (0, 0), (2, 2) ]) == 2)
	assert(proc([ (0, 0), (2, 3) ]) == 3)
	assert(proc([ (0, 0), (0, 3) ]) == 3)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve([ l for l in fileinput.input() ], verbose=True)
