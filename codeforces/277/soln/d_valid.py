import fileinput

def proc_input(args):
	(d, n) = [ int(x) for x in args[0].split() ]
	terms = [ int(x) for x in args[1].split() ]
	# 1-indexed
	weights = { i + 1 : terms[i] for i in xrange(n) }
	adjacency_list = { i + 1 : [] for i in xrange(n) }
	if n > 1:
		for l in args[2:2 + n]:
			(p, c) = [ int(x) for x in l.split() ]
			# build up neighbors
			adjacency_list[p].append(c)
			adjacency_list[c].append(p)
	return(d, n, weights, adjacency_list)

valid = {}
visited = {}
mod_base = 10 ** 9 + 7

def dfs(d, weights, adjacency_list, cur, root):
	global valid, visited, mod_base
	visited[cur] = True
	valid[cur] = 1
	for neighbor in adjacency_list[cur]:
		if visited[neighbor]:
			continue
		# testing for bounds -- assert that weight[cur] is minimum weight in the set so far
		#	this way, we won't double-count nodes with weight[n] < weight[cur] which will also belong in this set
		if not (weights[root] <= weights[neighbor] <= weights[root] + d):
			continue
		# prevent double counting (for the remaining case of equal weights)
		if (weights[root] == weights[neighbor] and neighbor < root):
			continue
		valid[cur] = (valid[cur] * (dfs(d, weights, adjacency_list, neighbor, root) + 1)) % mod_base
	return valid[cur]

# return number of valid subsets for given node, via DFS search
def get_valid(d, n, weights, adjacency_list, node):
	global valid, visited
	valid = { i + 1 : 0 for i in xrange(n) }
	visited = { i + 1 : False for i in xrange(n) }
	return(dfs(d, weights, adjacency_list, node, node))

def solve(args, verbose=False):
	global mod_base
	(d, n, weights, adjacency_list) = proc_input(args)
	results = 0
	for node in weights.keys():
		results = (results + get_valid(d, n, weights, adjacency_list, node)) % mod_base
	if verbose:
		print results
	return(results)

def test():
	assert(proc_input([ '0 1', '2', '' ]) == (0, 1, { 1 : 2 }, { 1 : [] }))
	assert(proc_input([ '0 2', '3 4', '1 2' ]) == (0, 2, { 1 : 3, 2 : 4 }, { 1 : [ 2 ], 2 : [ 1 ] }))
	assert(solve([ '1 4', '2 1 3 2', '1 2', '1 3', '3 4' ]) == 8)
	assert(solve([ '0 3', '1 2 3', '1 2', '2 3' ]) == 3)
	assert(solve([ '4 8', '7 8 7 5 4 6 4 10', '1 6', '1 2', '5 8', '1 3', '3 5', '6 7', '3 4' ]) == 41)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve([ l for l in fileinput.input() ], verbose=True)
