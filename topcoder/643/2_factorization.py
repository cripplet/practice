class TheKingsFactorization(object):
	def getVector(self, n, ps):
		ps = [ int(x) for x in ps ]
		n /= reduce(lambda x, y: x * y, ps)
		div = ps[0]
		fac = sorted(ps)
		while div ** 2 <= n and div < ps[-1]:
			while n % div == 0:
				fac.append(div)
				n /= div
			div += 2
		if n > 1:
			fac.append(n)
		return sorted(fac)

print TheKingsFactorization().getVector(12, ["2","3"])
