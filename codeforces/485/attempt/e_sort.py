import fileinput

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	s = args[0].strip()
	n = int(args[1])
	ops = []
	for l in args[2:]:
		ops.append(tuple([ int(x) for x in l.split() ]))
	return(s, n, ops)

def proc(s_list, k, d):
	for i in xrange(len(s_list) - k + 1):
		buckets = [ [] for bucket in xrange(d) ]
		for index in xrange(i, i + k):
			buckets[(index - i) % d].append(s_list[index])
		index = i
		for bucket in buckets:
			s_list[index:index + len(bucket)] = bucket
			index += len(bucket)
	return(s_list)

def solve(args, verbose=False):
	(s, n, ops) = proc_input(args)
	s_list = list(s)
	acc = []
	for (k, d) in ops:
		proc(s_list, k, d)
		acc.append(''.join(s_list))
	if verbose:
		for l in acc:
			print l
	return(acc)

def test():
	assert(proc_input([ 'qwerty', '3', '4 2', '6 3', '5 2' ]) == ('qwerty', 3, [ (4, 2), (6, 3), (5, 2) ]))
	assert(proc(list('qwerty'), 4, 2) == list('qertwy'))
	assert(solve([ 'qwerty', '3', '4 2', '6 3', '5 2' ]) == ([ 'qertwy', 'qtewry', 'qetyrw' ]))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
