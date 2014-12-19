import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(str_to_int(args[0]))

def solve(args, verbose=False):
	(cnt_x, cnt_y, x, y) = proc_input(args)
	forbid_x = set([ i * x for i in xrange(1, cnt_x + cnt_y) ])
	forbid_y = set([ i * y for i in xrange(1, cnt_x + cnt_y) ])
	set_x = [ 1 ] * cnt_x
	set_y = [ 1 ] * cnt_y
	count_x = count_y = 0
	i = 1
	if cnt_x > cnt_y:
		count_x += 1
	else:
		count_y += 1
	while count_x < cnt_x or count_y < cnt_y:
		i += 1
		if (i not in forbid_x) and (count_x < cnt_x):
			set_x[count_x] = i
			count_x += 1
		elif (i not in forbid_y) and (count_y < cnt_y):
			set_y[count_y] = i
			count_y += 1
	if verbose:
		print i
	return(i)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '3 1 2 3' ]) == 5)
	assert(solve([ '1 3 2 3' ]) == 4)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
