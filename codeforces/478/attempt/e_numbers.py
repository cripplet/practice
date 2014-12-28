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

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(stoi(args[0]))

def wavy_aux(n, prev, increase):
	test = n % 10
	if (increase and prev < test) or (not increase and prev > test):
		if n < 10:
			return True
		return wavy_aux(n / 10, test, not increase)
	else:
		return False
		

def wavy(n):
	if n < 10:
		return True
	return(wavy_aux(n / 10, n % 10, (n / 10) % 10 > n % 10))

def solve(args, verbose=False):
	(n, k) = proc_input(args)
	(kp, tn) = (0, n)
	while tn < 10 ** 14 and kp < k:
		tn += n
		if wavy(tn):
			kp += 1

	r = -1
	if tn < 10 ** 14 and kp == k:
		r = tn

	if verbose:
		print r
	return r

def test():
	assert(wavy(2) == True)
	assert(wavy(22) == False)
	assert(wavy(121) == True)
	assert(wavy(212) == True)
	assert(solve([ '123 4' ]) == 1845)
	assert(solve([ '100 1' ]) == -1)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
