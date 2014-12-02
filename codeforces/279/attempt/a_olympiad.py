import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return str_to_int(args[1])

def solve(args, verbose=False):
	talents = proc_input(args)
	counter = { 1 : [], 2 : [], 3 : [] }
	for k, v in enumerate(talents):
		counter[v].append(k + 1)
	max_teams = min([ len(counter[x]) for x in counter ])
	if verbose:
		print max_teams
	if max_teams == 0:
		return max_teams
	r = []
	for i in xrange(max_teams):
		t = tuple([ counter[x].pop() for x in counter ])
		if verbose:
			print ' '.join([ str(x) for x in t ])
		r.append(t)
	return (max_teams, r)

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '7', '1 3 1 3 2 1 2' ]) == (2, [ (6, 7, 4), (3, 5, 2) ]))
	assert(solve([ '4', '2 1 1 2' ]) == 0)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
