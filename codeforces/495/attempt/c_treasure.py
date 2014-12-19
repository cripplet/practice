import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(args[0].strip())

def solve(args, verbose=False):
	s = proc_input(args)
	p_last = s.rfind('#')
	n_nest = 0
	succ = True
	for p, c in enumerate(s):
		if c == '(':
			n_nest += 1
		if c == ')' or (c == '#'):
			n_nest -= 1
			if n_nest < 0:
				succ = False
				break
	result = [ -1 ]
	if succ:
		result = [ 1 ] * s.count('#')
		result[-1] += n_nest
		# check
		n_p = 0
		n_nest = 0
		for p, c in enumerate(s):
			if n_nest < 0:
				result = [ -1 ]
				break
			if c == '(':
				n_nest += 1
			if c == ')':
				n_nest -= 1
			if c == '#':
				n_nest -= result[n_p]
				n_p += 1
	if verbose:
		for x in result:
			print x
	return result

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '(((#)((#)' ]) == [ 1, 2 ])
	assert(solve([ '()((#((#(#()' ]) == [ 1, 1, 3 ])
	assert(solve([ '#' ]) == [ -1 ])
	assert(solve([ '(#)' ]) == [ -1 ])
	assert(solve([ '((#)(' ]) == [ -1 ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
