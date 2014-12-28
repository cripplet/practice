class TheKingsArmyDiv2(object):
	def getNumber(self, state):
		last = [ '' ] * len(state[0])
		happ = cons = False
		for row in state:
			happ = max(happ, 'H' in row)
			cl = [ last[i] + row[i] for i in xrange(len(row)) ]
			cons = max(cons, 'HH' in row or 'HH' in cl)
			last = list(row)
		return 2 - (happ + cons)

print TheKingsArmyDiv2().getNumber(["SSSSS","SSHHS","SSSSS"])
