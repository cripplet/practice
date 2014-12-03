import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return tuple(str_to_int(args[0]))

def find_min(m, s, first=0):
	if m == 0:
		return ''
	if (9 * m < s) or (s <= 0 and first == 1):
		return '-1'
	r = max(first, s - (9 * (m - 1))) # min FIRST digit such that m, s is still valid
	return str(r) + find_min(m - 1, s - r)

def find_max(m, s):
	if m == 0:
		return ''
	r = min(9, s) # max FIRST digit such that m, s is still valid
	return str(r) + find_max(m - 1, s - r)

def solve(args, verbose=False):
	(m, s) = proc_input(args)
	_min = find_min(m, s, 1)
	_max = '-1'
	if _min != '-1':
		_max = find_max(m, s)
	# special case
	if m == 1 and s == 0:
		(_min, _max) = ('0', '0')
	if verbose:
		print int(_min), int(_max)
	return (int(_min), int(_max))

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '2 15' ]) == (69, 96))
	assert(solve([ '2 0' ]) == (-1, -1))
	assert(solve([ '2 19' ]) == (-1, -1))
	assert(solve([ '2 1' ]) == (10, 10))
	assert(solve([ '3 10' ]) == (109, 910))
	assert(solve([ '1 0' ]) == (0, 0))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
