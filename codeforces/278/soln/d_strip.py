import fileinput

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, s, l) = [ int(x) for x in args[0].split() ]
	strip = [ int(x) for x in args[1].split() ]
	return(n, s, l, strip)

G = {}
F = {}
def gen(strip, min_el, max_rng):
	global G
	G = {}
	for i in xrange(len(strip)):
		w = i
		G[i] = 0
		_max = _min = strip[w]
		while _max - _min <= max_rng:
			G[i] += 1
			if w == 0:
				break
			w -= 1
			_max = max(_max, strip[w])
			_min = min(_min, strip[w])
		if G[i] < min_el:
			G[i] = -1
	return G

def proc(strip, min_el, max_rng):
	gen(strip, min_el, max_rng)
	global G, F
	F = {}
	assert(G[min_el - 1] == -1 or G[min_el - 1] == min_el)
	for i in xrange(len(strip)):
		if i < min_el - 1:
			F[i] = 0
		elif G[i] == -1:
			F[i] = -1
		elif i == min_el - 1:
			F[i] = 1
		else:
			_min = max(0, i - G[i])
			_max = max(0, i - min_el)
			F[i] = min([ F[k] for k in xrange(_min, _max + 1) ]) + 1
	return F

def solve(args, verbose=False):
	(n, max_rng, min_el, strip) = proc_input(args)
	proc(strip, min_el, max_rng)
	global F
	r = F[len(F) - 1]
	if verbose:
		print r
	return r

def test():
	assert(gen([ 0, 1, 2, 3 ], 1, 0) == { 0 : 1, 1 : 1, 2 : 1, 3 : 1 })
	assert(gen([ 0, 100, 0, 100 ], 2, 1) == { 0 : -1, 1 : -1, 2 : -1, 3 : -1 })
	assert(gen([ 0, 100, 1, 1 ], 2, 1) == { 0 : -1, 1 : -1, 2 : -1, 3 : 2 })
	assert(gen([ 0, 1, 0, 1 ], 2, 1) == { 0 : -1, 1 : 2, 2 : 3, 3 : 4 })
	assert(solve([ '7 2 2', '1 3 1 2 4 1 2' ]) == 3)
	assert(solve([ '7 2 2', '1 100 1 100 1 100 1' ]) == -1)
	assert(solve([ '1 0 1', '0' ]) == 1)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
