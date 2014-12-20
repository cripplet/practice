import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, k) = str_to_int(args[0])
	h = str_to_int(args[1])
	return(n, k, h)
		
def solve(args, verbose=False):
	(n, k, h) = proc_input(args)
	h = [ [ x, y + 1 ] for y, x in enumerate(h) ]
	h.sort(key=lambda(x, y): x)
	log = []
	m = 0
	while (h[0][0] != h[-1][0]) and m < k:
		h[0][0] += 1
		h[-1][0] -= 1
		log.append((h[-1][1], h[0][1]))
		h.sort(key=lambda(x, y): x)
		m += 1
	s = h[-1][0] - h[0][0]
	if verbose:
		print s, m
		for (a, b) in log:
			print a, b
	return(s, m, log)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '3 2', '5 8 5' ]) == (0, 2, [ (2, 1), (2, 3) ]))
	solve([ '5 3', '8 3 2 6 3' ], verbose=True)


if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
