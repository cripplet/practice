import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, m) = str_to_int(args[0])
	strings = [ args[i + 1].strip() for i in xrange(n) ]
	return(n, m, strings)

def solve(args, verbose=False):
	(n, m, strings) = proc_input(args)
	acc = [ '' ] * n
	r = 0
	for i in xrange(m):
		rollback = False
		for j in xrange(n):
			acc[j] += strings[j][i]
		for j in xrange(n - 1):
			if acc[j + 1] < acc[j]:
				r += 1
				rollback = True
				break
		if rollback:
			for j in xrange(n):
				acc[j] = acc[j][:-1]
	if verbose:
		print r
	return r
			
			

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(proc_input([ '1 10', 'codeforces' ]) == (1, 10, [ 'codeforces' ]))
	assert(solve([ '1 10', 'codeforces' ]) == 0)
	assert(solve([ '4 4', 'case', 'care', 'test', 'code' ]) == 2)
	assert(solve([ '5 4', 'code', 'forc', 'esco', 'defo', 'rces' ]) == 4)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
