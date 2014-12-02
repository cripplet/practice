import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, r, avg) = str_to_int(args[0])
	lst = []
	for l in args[1:]:
		lst.append(list(str_to_int(l)))
	return (n, r, avg, lst)

def solve(args, verbose=False):
	(n, r, avg, lst) = proc_input(args)
	n_b = 0
	cur_avg = sum([ x[0] for x in lst ])
	if cur_avg < avg * n:
		lst.sort(key=lambda x: x[1])
		for (a, b) in lst:
			# add as many elements as possible
			new = min(avg * n - cur_avg, r - a)
			n_b += new * b
			cur_avg += new
			if avg * n <= cur_avg:
				break
	if verbose:
		print n_b
	return n_b

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(proc_input([ '2 0 1', '4 7', '6 5' ]) == (2, 0, 1, [ [ 4, 7 ], [ 6, 5 ] ]))
	assert(solve([ '5 5 4', '5 2', '4 7', '3 1', '3 2', '2 5' ]) == 4)
	assert(solve([ '2 5 4', '5 2', '5 2' ]) == 0)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
