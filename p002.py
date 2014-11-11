CACHE = [ 1, 1 ]
def gen_fib(bound):
	x = CACHE[-2]
	y = CACHE[-1]
	while x + y < bound:
		CACHE.append(x + y)
		x = y
		y = CACHE[-1]

def sum_even_fib(bound):
	gen_fib(bound)
	acc = 0
	for x in CACHE:
		if(x < bound) and (x & 1 == 0):
			acc += x
	return acc

def main(bound):
	return sum_even_fib(bound)

if __name__ == '__main__':
	gen_fib(0)
	assert(CACHE == [ 1, 1 ])
	gen_fib(10)
	assert(CACHE == [ 1, 1, 2, 3, 5, 8 ])
	assert(sum_even_fib(0) == 0)
	assert(sum_even_fib(10) == 10)
	print main(4000000)
