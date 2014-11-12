import fileinput

def proc_args(args):
	known_size = False
	s = ''
	p = ''
	s_l = 0
	for l in args:
		if not known_size:
			(s_l, p) = [ int(x) for x in l.split() ]
			# p is 1-indexed in given text
			p -= 1
			known_size = True
		else:
			s = l.strip()
	return(s_l, p, s)

# gets reverse complement char from string (given forward index less than half of str len)
def get_complement(s, i):
	if i > len(s) / 2 or len(s) == 0 or i < 0:
		return ''
	return s[-i - 1]

def get_index_bound(s, p):
	l = r = p
	for i in xrange(0, len(s) / 2):
		if(s[i] != get_complement(s, i)):
			if i < l and i <= p:
				l = i
			if i >= p and ((r == None) or (i > r)):
				r = i
	return(l, r)

def solve(args, verbose=False):
	(s_l, p, s) = proc_args(args)
	# WLOG, p in the first half of the string
	if p >= len(s) / 2:
		p = len(s) - 1 - p
	(l, r) = get_index_bound(s, p)
	steps = r - l + min(r - p, p - l)
	for i in xrange(l, r + 1):
		(_s, _t) = (s[i], get_complement(s, i))
		if(_s != _t):
			delta = max(ord(_s), ord(_t)) - min(ord(_s), ord(_t))
			steps += min(delta, 26 - delta)
	if verbose:
		print steps
	return steps
	
def test():
	assert(proc_args([ '8 3', 'abcdefgh' ]) == (8, 2, 'abcdefgh'))
	assert(get_complement('', 0) == '')
	assert(get_complement('abc', 2) == '')
	assert(get_complement('ab', 0) == 'b')
	assert(get_complement('abc', 1) == 'b')
	assert(get_complement('abc', 0) == 'c')
	assert(get_index_bound('a', 0) == (0, 0))
	assert(get_index_bound('ab', 0) == (0, 0))
	assert(get_index_bound('abc', 0) == (0, 0))
	assert(get_index_bound('abc', 1) == (0, 1))
	assert(get_index_bound('aeabcaez', 2) == (0, 3))
	assert(solve([ '8 3', 'aeabcaez' ]) == 6)
	assert(solve([ '8 6', 'aeabcaez' ]) == 6)
	assert(solve([ '39 30', 'yehuqwaffoiyxhkmdipxroolhahbhzprioobxfy' ]) == 138)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(fileinput.input(), verbose=True)
