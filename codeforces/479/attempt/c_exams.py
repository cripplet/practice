import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	dates = []
	for l in args[1:]:
		dates.append(str_to_int(l))
	return dates

def solve(args, verbose=False):
	dates = proc_input(args)
	dates.sort()
	cur_last = -1
	for (a, b) in dates:
		if min(a, b) >= cur_last:
			cur_last = min(a, b)
		else:
			cur_last = max(a, b)
	if verbose:
		print cur_last
	return cur_last

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '3', '5 2', '3 1', '4 2' ]) == 2)
	assert(solve([ '3', '6 1', '5 2', '4 3' ]) == 6)
	assert(solve([ '5', '4 3', '4 2', '4 1', '4 1', '4 1' ]) == 3)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
