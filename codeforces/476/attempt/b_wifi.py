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

def tolerance(s, t, r=10 ** -6):
	return t - r <= s <= t + r

###          ###
# code follows #
###          ###

def c(n, k):
	if n < k:
		return 0
	return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return([ list(l.strip()) for l in args ])

def solve(args, verbose=False):
	(drazil, dreamoon) = proc_input(args)
	n_plus = drazil.count('+')
	n_interpreted = dreamoon.count('+')
	n_guesses = dreamoon.count('?')
	p_succ = int((n_plus == n_interpreted))
	if n_guesses > 0 and n_plus >= n_interpreted:
		p_succ = c(n_guesses, n_plus - n_interpreted) / float(2 ** n_guesses)
	if verbose:
		print p_succ
	return p_succ

def test():
	assert(tolerance(solve([ '++-+-', '+-+-+' ]), 1, 10 ** -9))
	assert(tolerance(solve([ '+-+-', '+-??' ], verbose=True), .5, 10 ** -9))
	assert(tolerance(solve([ '+++', '??-' ], verbose=True), 0, 10 ** -9))
	assert(tolerance(solve([ '----------', '+++?++++-+' ], verbose=True), 0, 10 ** -9))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
