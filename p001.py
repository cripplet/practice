def mult(x, rng):
	acc = []
	if x == 0:
		return acc
	i = x
	while i < rng:
		acc.append(i)
		i += x
	return acc

def main(bound, terms=[]):
	return sum([sum(mult(i, bound)) for i in terms]) - sum(mult(3 * 5, bound))

if __name__ == '__main__':
	assert(mult(0, 10) == [])
	assert(mult(1, 10) == [ x + 1 for x in xrange(9) ])
	assert(mult(1, 0) == [])
	assert(mult(3, 10) == [ 3, 6, 9 ])
	assert(mult(5, 10) == [ 5 ])
	assert(main(10, [ 3, 5 ]) == 23)
	assert(main(10, [ 1 ]) == 45)
	print main(1000, [ 3, 5 ])
