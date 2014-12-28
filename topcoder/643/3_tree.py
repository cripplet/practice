from Queue import Queue
class Node(object):
	def __init__(self):
		# True == G
		self.color = None
		self.cache = { True : 0, False : 0 }
		self.p = None
		self.child = []
	def update(self, color):
		self.cache[color] += 1
		if self.p is not None:
			self.p.update(color)
	def paint(self, color):
		self.color = color
		self.update(color)
	@property
	def cost(self):
		if self.color is None:
			return 0
		return self.cache[self.color]
	def reset(self):
		self.cache[True] = self.cache[False] = 0
		for c in self.child:
			c.reset()

class TheKingsTree(object):
	def getNumber(self, ps):
		nodes = [ Node() for x in xrange(len(ps) + 1) ]
		ps = [ int(x) for x in ps ]
		for k, p in enumerate(ps):
			nodes[k + 1].p = nodes[p]
			nodes[p].child.append(nodes[k + 1])
		red = self.getN(nodes[0], False)
		nodes[0].reset()
		gre = self.getN(nodes[0], True)
		return(min(red, gre))

	def getN(self, root, c):
		Q = Queue()
		Q.put(root)
		while not Q.empty():
			node = Q.get()
			if node == root:
				node.paint(c)
			else:
				node.paint(not node.p.color)
			for c in node.child:
				Q.put(c)
		Q = Queue()
		Q.put(root)
		cost = 0
		while not Q.empty():
			node = Q.get()
			cost += node.cost
			for c in node.child:
				Q.put(c)
		print cost
		return cost

print TheKingsTree().getNumber([ '0', '0', '0' ])
print TheKingsTree().getNumber([ '0', '1', '2', '3', '1' ])
