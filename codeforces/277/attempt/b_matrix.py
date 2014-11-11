import fileinput

def read_input(lines=None):
	m = 0
	n = 0
	size_known = False
	b = []
	if lines == None:
		lines = fileinput.input()
	for line in lines:
		x = [ int(x) for x in line.split() ]
		if not size_known:
			m = x[0]
			n = x[1]
			size_known = True
		else:
			b.append(x)
	return(m, n, b)

# assert(read_input([ '2 2', '1 0', '0 0' ]) == (2, 2, [ [ 1, 0 ], [ 0, 0 ] ]))
# assert(read_input([ '2 3', '1 1 1', '1 1 1' ]) == (2, 3, [ [ 1, 1, 1 ], [ 1, 1, 1 ] ]))

def get_candidates(b):
	col_candidates = []
	row_candidates = []

	m = len(b)
	if m != 0:
		n = len(b[0])
	else:
		n = 0
	if m == 0 or n == 0:
		return(row_candidates, col_candidates)

	for c_index in xrange(n):
		if b[0][c_index] and sum([ r[c_index] for r in b ]) == m:
			col_candidates.append(c_index)

	for r_index in xrange(m):
		if b[r_index][0] and sum(b[r_index]) == n:
			row_candidates.append(r_index)

	return(row_candidates, col_candidates)

# assert(get_candidates([ [ 0 ] ]) == ( [], [] ))
# assert(get_candidates([ [ 1 ] ]) == ( [ 0 ], [ 0 ] ))
# assert(get_candidates([ [ 0, 1, 1, 0 ], [ 1, 1, 1, 1 ] ]) == ( [ 1 ], [ 1, 2 ] ))

def check_candidates(m, n, r, c, b):
	if m == 0 or n == 0:
		return False

	if(len(r) == 0 and len(c) > 0) or (len(c) == 0 and len(r) > 0):
		return False
	results = []
	for r_index in xrange(m):
		for c_index in xrange(n):
			if(b[r_index][c_index]):
				if r_index not in r and c_index not in c:
					return False
				if r_index in r and c_index in c:
					results.append((r_index, c_index))
			else:
				if r_index in r or c_index in c:
					return False
	return(True, results)

# assert(check_candidates(1, 1, [ 0 ], [ 0 ], [ [ 1 ] ]) == (True, [ (0, 0) ]))
# assert(check_candidates(1, 1, [], [], [ [ 0 ] ]) == (True, []))
# assert(check_candidates(2, 2, [], [], [ [ 1, 0 ], [ 0, 0 ] ]) == False)
# assert(check_candidates(2, 3, [ 0, 1 ], [ 0, 1, 2 ], [ [ 1, 1, 1 ], [ 1, 1, 1 ] ]) == (True, [ (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2) ]))
# assert(check_candidates(2, 3, [ 1 ], [ 1 ], [ [ 0, 1, 0 ], [ 1, 1, 1 ] ]) == (True, [ (1, 1) ]))

def get_a(m, n, ones):
	a = [ [ 0 for c in xrange(n) ] for r in xrange(m) ]
	for x in ones:
		a[x[0]][x[1]] = 1
	return a

def calc(b=None):
	if b == None:
		(m, n, b) = read_input()
	else:
		m = len(b)
		if m == 0:
			n = 0
		else:
			n = len(b[0])
	(r_c, c_c) = get_candidates(b)
	valid = check_candidates(m, n, r_c, c_c, b)
	if valid == False:
		print 'NO'
	else:
		print 'YES'
		a = get_a(m, n, valid[1])
		print '\n'.join([ ' '.join([ str(c) for c in r ]) for r in a ])

# calc(b=[ [ 1 for x in xrange(100) ] for x in xrange(100) ])
calc()
