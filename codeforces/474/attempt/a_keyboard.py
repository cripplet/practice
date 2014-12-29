import fileinput, math

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

def perm(n, k, wheels=True):
	if wheels:
		assert(n > 0)
		assert(k > 0)
	return math.factorial(n) / math.factorial(k)

def comb(n, k, wheels=True):
	if wheels:
		assert(n > 0)
		assert(k > 0)
		assert(n - k > 0)
	return perm(n, k, False) / math.factorial(n - k)

def tol(actual, expected, tolerance=10 ** -9):
	return expected - tolerance <= actual <= expected + tolerance

def _sigma(f):
	return f * (f + 1) / 2

# sum(x from i to f)
def sigma(i, f, wheels=True):
	if wheels:
		assert(i >= 0)
		assert(f >= 0)
	return _sigma(f) - _sigma(i - 1)

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	d = args[0].strip()
	s = args[1].strip()
	return(d, s)

def solve(args, verbose=False):
	(d, s) = proc_input(args)
	d = 2 * (d == 'L') - 1
	a = 'qwertyuiopasdfghjkl;zxcvbnm,./'
	# reverse lookup
	b = dict(zip(a, range(len(a))))
	r = ''.join([ a[b[c] + d] for c in s ])
	if verbose:
		print r
	return r

def test():
	assert(_sigma(10) == 55)
	assert(sigma(3, 10) == 52)
	assert(sigma(1, 1) == 1)
	assert(sigma(3, 4) == 7)
	assert(solve([ 'R', 's;;upimrrfod;pbr' ], verbose=True) == 'allyouneedislove')

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
