import fileinput

###          ###
# utility func #
###          ###

dbug = True

def stoi(s):
	return([ int(x) for x in s.split() ])

def pd(s, label=''):
	global dbug
	if dbug:
		header = 'debug:'
		if label != '':
			header += ' (%s)\t' % label
		print header, s

###          ###
# code follows #
###          ###

FACTORIAL = [ 1, 1 ]
def fac(n):
	global FACTORIAL
	while len(FACTORIAL) <= n:
		FACTORIAL.append(FACTORIAL[-1] * len(FACTORIAL))
	return FACTORIAL[n]

def com(n, k):
	if k == 2:
		return(n * (n - 1) / 2)
	return fac(n) / (fac(k) * fac(n - k))

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(stoi(args[0]))

def solve(args, verbose=False):
	(n, m) = proc_input(args)
	(b, nb) = (n / m, m - n % m)
	(f, nf) = (b + 1, m - nb)
	k_min = com(b, 2) * nb + com(f, 2) * nf
	k_max = com(n - (m - 1), 2)
	if verbose:
		print k_min, k_max
	return k_min, k_max

def test():
	assert(fac(0) == fac(1) == 1)
	assert(fac(2) == 2)
	assert(fac(3) == 6)
	assert(com(5, 2) == 10)
	assert(solve([ '5 1' ]) == (10, 10))
	assert(solve([ '3 2' ]) == (1, 1))
	assert(solve([ '6 3' ]) == (3, 6))
	assert(solve([ '5 3' ]) == (2, 3))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
