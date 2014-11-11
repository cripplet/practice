import math

def gen_sieve(bound):
	s = [ True for x in xrange(bound) ]
	SIEVE = []
	s[0] = False
	s[1] = False
	for x in xrange(2, bound):
		if s[x] == True:
			SIEVE.append(x)
			t = 2 * x
			while t < bound:
				s[t] = False
				t += x
	return SIEVE

def factors(candidates, target):
	result = []
	for x in candidates:
		if x != 0:
			if target % x == 0:
				result.append(x)
	return result

def main(x):
	s = gen_sieve(int(math.sqrt(x)))
	return factors(s, x)[-1]

if __name__ == '__main__':
	print gen_sieve(10)
	assert(gen_sieve(10) == [ 2, 3, 5, 7 ])
	assert(factors([], 0) == [])
	assert(factors([ 0, 2 ], 10) == [ 2 ])
	assert(factors([ 1 ], 10) == [ 1 ])
	assert(factors([ 1, 2, 3, 4, 5, 6 ], 24) == [ 1, 2, 3, 4, 6 ])
	print main(600851475143)
