import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	f = str_to_int(args[1])
	s = str_to_int(args[3])
	return (f, s)

def solve(args, verbose=False):
	(f, s) = proc_input(args)
	post = [ ('f', x) for x in f ] + [ ('s', x) for x in s ]
	# sort by shot distance
	post.sort(key=lambda x: x[1])
	n_f = n_s = 0
	max_a = 3 * len(f)
	res_b = 3 * len(s)
	max_diff = max_a - res_b
	last = None
	for x in xrange(len(post)):
		t = post[x]
		if t[0] == 'f':
			n_f += 1
		else:
			n_s += 1
		if t != last:
			a = 2 * n_f + (3 * (len(f) - n_f))
			b = 2 * n_s + (3 * (len(s) - n_s))
			diff = a - b
			if diff > max_diff:
				max_a = a
				res_b = b
				max_diff = diff
			elif diff == max_diff:
				if a > max_a:
					max_a = a
					res_b = b
			last = t
	if verbose:
		print '%s:%s' % (max_a, res_b)
	return (max_a, res_b)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '3', '1 2 3', '2', '5 6' ]) == (9, 6))
	assert(solve([ '5', '6 7 8 9 10', '5', '1 2 3 4 5' ]) == (15, 10))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
