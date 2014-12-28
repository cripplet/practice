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
	(n, m) = stoi(args[0])
	words = {}
	for l in args[1:-1]:
		(a, b) = l.strip().split()
		words[a] = b
	speech = args[-1].strip().split()
	return(n, m, words, speech)

def solve(args, verbose=False):
	(n, m, words, speech) = proc_input(args)
	notes = []
	for w in speech:
		wp = w
		(la, lb) = (len(w), len(words[w]))
		if la > lb:
			wp = words[w]
		notes.append(wp)
	if verbose:
		print ' '.join(notes)
	return notes

def test():
	assert(solve([ '4 3', 'codeforces codesecrof', 'contest round', 'letter message', 'codeforces contest letter contest' ]) == 'codeforces round letter round'.split())
	assert(solve([ '5 3', 'joll wuqrd', 'euzf un', 'hbnyiyc rsoqqveh', 'hbnyiyc joll joll euzf joll' ]) == 'hbnyiyc joll joll un joll'.split())


if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
