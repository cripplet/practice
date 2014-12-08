import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	radii = str_to_int(args[1])
	coord = []
	for l in args[3:]:
		coord.append(tuple(str_to_int(l)))
	return(radii, coord)

from bisect import bisect_left

# http://stackoverflow.com/questions/212358/binary-search-in-python
def binary_search(a, x, lo=0, hi=None):
	hi = hi if hi is not None else len(a)
	pos = bisect_left(a, x, lo, hi)
	return (pos if pos != hi and a[pos] == x else -1)

def solve(args, verbose=False):
	(r, c) = proc_input(args)
	r.sort()
	r = [ x ** 2 for x in r ]
	s = []
	for (i, j, k, l) in c:
		ti = i ** 2 + j ** 2
		tf = k ** 2 + l ** 2
		r_i = min(ti, tf)
		r_f = max(ti, tf)
		s.append((r_i, r_f))

	ct = 0

	for (r_b, r_e) in s:
		l_ind = bisect_left(r, r_b)
		r_ind = bisect_left(r, r_e)
		ct += r_ind - l_ind

	if verbose:
		print ct
	return ct

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(proc_input([ '4', '1 2 3 4', '3', '1 -1 4 -3', '2 1 1 2', '1 -2 3 -4' ]) == ([ 1, 2, 3, 4 ], [ (1, -1, 4, -3), (2, 1, 1, 2), (1, -2, 3, -4) ]))
	assert(solve([ '4', '1 2 3 4', '3', '1 -1 4 -3', '2 1 1 2', '1 -2 3 -4' ], verbose=True) == 5)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
