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
	(hx, hy) = stoi(args[0])
	(ux, uy) = stoi(args[1])
	lines = []
	for l in args[3:]:
		lines.append(stoi(l))
	return((hx, hy), (ux, uy), lines)

# generate two points
# ax + by + c = 0
def gen((a, b, c)):
	if b != 0:
		pts = [ (0, -c / b), (1, (-c - 1) / b) ]
	elif a != 0:
		pts = [ (-c / a, 0), ((-c - 1) / a, 1) ]
	return pts

# | a b |
# | c d |
def det(a, b, c, d):
	return a * d - b * c

def d((a, b), (c, d)):
	return ((a - c) ** 2 + (b - d) ** 2) ** 0.5

# None if parallel, else returns intersection point
def pt((hx, hy), (ux, uy), (a, b, c)):
	((x3, y3), (x4, y4)) = gen((a, b, c))
	denom = det( det(hx, 1, ux, 1), det(hy, 1, uy, 1), det(x3, 1, x4, 1), det(y3, 1, y4, 1) )
	if denom == 0:
		return None
	x = float(det( det(hx, hy, ux, uy), det(hx, 1, ux, 1), det(x3, y3, x4, y4), det(x3, 1, x4, 1) ))
	y = float(det( det(hx, hy, ux, uy), det(hy, 1, uy, 1), det(x3, y3, x4, y4), det(y3, 1, y4, 1) ))
	return(x / denom, y / denom)

def solve(args, verbose=False):
	(h, u, lines) = proc_input(args)
	counter = 0
	for l in lines:
		r = pt(h, u, l)
		if r is not None:
			if d(h, r) < d(h, u) and d(u, r) < d(h, u):
				counter += 1
	if verbose:
		print counter
	return counter

def test():
	assert(solve([ '1 1', '-1 -1', '2', '0 1 0', '1 0 0' ]) == 2)
	assert(solve([ '1 1', '-1 -1', '3', '1 0 0', '0 1 0', '1 1 -3' ]) == 2)
	assert(solve([ '1 0', '-1 0', '3', '0 1 0', '0 2 0', '0 -1 0' ]) == 3)
	assert(solve([ '2 2', '-2 -2', '3', '1 0 0', '0 1 0', '1 1 -1' ]) == 3)
	assert(solve([ '1 0', '0 0', '2', '1 0 3', '1 0 4' ]) == 0)
	assert(solve([ '0 1', '0 0', '2', '0 1 3', '0 1 4' ]) == 0)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
