import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	bs = str_to_int(args[1])
	gs = str_to_int(args[3])
	return(bs, gs)

def find(bv, gs):
	tgt = -1
	for k, v in enumerate(gs):
		if abs(bv - v) <= 1:
			tgt = k
			break
	if tgt != -1:
		gs.pop(tgt)
	return tgt
		

def solve(args, verbose=False):
	(x, y) = proc_input(args)
	bs = list(x)
	gs = list(y)
	bs.sort()
	gs.sort()
	count = 0
	for bk in xrange(len(bs)):
		r = find(bs[bk], gs)
		if r != -1:
			count += 1
	if verbose:
		print count
	return count

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '4', '1 4 6 2', '5', '5 1 5 7 9' ]) == 3)
	assert(solve([ '4', '1 2 3 4', '4', '10 11 12 13' ]) == 0)
	assert(solve([ '5', '1 1 1 1 1', '3', '1 2 3' ]) == 2)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
