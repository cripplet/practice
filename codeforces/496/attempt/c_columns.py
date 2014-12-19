import fileinput

class S(object):
	_index = set()
	def __init__(self, s):
		self.s = list(s)
	@staticmethod
	def add_index(i):
		S._index.add(i)
	@property
	def r(self):
		r = ''
		for k, v in enumerate(self.s):
			if k not in S._index:
				r += v
		return r
	def __lt__(self, other):
		return self.r < other.r
	def __eq__(self, other):
		return self.r == other.r
	def __gt__(self, other):
		return self.r > other.r
	def __ne__(self, other):
		return not self.r == other.r
	def __getitem__(self, k):
		return self.s[k]

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, m) = str_to_int(args[0])
	strings = []
	for x in xrange(n):
		strings.append(S(args[x + 1].split()[0]))
	return(n, m, strings)

def solve(args, verbose=False):
	(n, m, strings) = proc_input(args)
	acc = 0
	for x in xrange(m):
		candidate = False
		for y in xrange(n - 1):
			if strings[y + 1] < strings[y]:
				candidate = True
		if candidate:
			for y in xrange(n - 1):
				if strings[y + 1][x] < strings[y][x]:
					S.add_index(x)
					break
	acc = len(S._index)
	if verbose:
		print acc
	return acc

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '1 10', 'codeforces' ]) == 0)
	assert(solve([ '4 4', 'case', 'care', 'test', 'code' ]) == 2)
	assert(solve([ '5 4', 'code', 'forc', 'esco', 'defo', 'rces' ]) == 4)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
