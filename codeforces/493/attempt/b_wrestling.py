import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	f = []
	s = []
	f_sum = s_sum = 0
	last = None
	for x in args[1:]:
		if int(x) > 0:
			f.append(int(x))
			f_sum += int(x)
			last = 'first'
		else:
			s.append(-int(x))
			s_sum += -int(x)
			last = 'second'
	return(f, s, f_sum, s_sum, last)

def solve(args, verbose=False):
	(f, s, fs, ss, l) = proc_input(args)
	if fs > ss:
		r = 'first'
	elif fs < ss:
		r = 'second'
	else:
		if f == s:
			r = l
		elif f > s:
			r = 'first'
		else:
			r = 'second'
	if verbose:
		print r
	return r

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '5', '1', '2', '-3', '-4', '3' ]) == 'second')
	assert(solve([ '3', '-1', '-2', '3' ]) == 'first')
	assert(solve([ '2', '4', '-4' ]) == 'second')
	assert(solve([ '4', '1', '-1', '2', '-2' ]) == 'second')
	assert(solve([ '4', '-1', '1', '-2', '2' ]) == 'first')

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
