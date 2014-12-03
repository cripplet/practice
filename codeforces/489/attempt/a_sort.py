import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return str_to_int(args[1])

def find(ints, offset):
	min = float('inf')
	min_index = -1
	for k, v in enumerate(ints[offset:]):
		if v < min:
			min = v
			min_index = k + offset
	return(min_index)

def swap(l, a, b):
	t = l[a]
	l[a] = l[b]
	l[b] = t

def solve(args, verbose=False, debug=False):
	ints = proc_input(args)
	if debug:
		from copy import deepcopy
		d = deepcopy(ints)
	results = []
	for i in xrange(len(ints)):
		min_index = find(ints, i)
		if min_index != i:
			results.append((min_index, i))
			swap(ints, min_index, i)
	if debug:
		d.sort()
		assert(ints == d)
		assert(len(results) <= len(ints))
	if verbose:
		print len(results)
		for (src, tgt) in results:
			print src, tgt
	return (len(results), results)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '5', '5 2 5 1 4' ], debug=True) == ( 2, [ (3, 0), (4, 2) ] ))
	assert(solve([ '6', '10 20 20 40 60 60' ], debug=True) == (0, []))
	assert(solve([ '2', '101 100' ], debug=True) == (1, [ (1, 0) ]))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
