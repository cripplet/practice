# http://en.wikipedia.org/wiki/Segment_tree
class Interval(object):
	def __init__(self, *args, **kwargs):
		self.l = None
		self.r = None
		self.c = None
		self.__dict__.update()
	@property
	def b(self):
		return(self.l, self.r)
	@b.setter
	def b(self, v):
		(self.l, self.r) = v

class SegmentTree(object):
	# expect interval to be of the form [ (l1, r1), (l2, r2), ... ]
	@staticmethod
	def build(intervals, sorted=False):
		if not sorted:
			intervals.sort(key=lambda(l, r): r)
		endpts = [ r for (l, r) in intervals ]
		nodes = []
		nodes.append(Tree(i=Interval(b=(-float('inf'), endpts[0]), c=True)))
		for k, v in enumerate(endpts):
			nodes.append(Tree(i=Interval(b=(v, v), c=open)))
			if k != len(endpts):
				nodes.append(Tree(i=Interval(b=(v, endpts[k + 1]), c=False)))
		nodes.append(Tree(i=Interval(b=(endpts[-1], float('inf')), c=True)))
		
		
	def __init__(self, *args, **kwargs):
		self.i = None
		self.l = None
		self.r = None
		self.__dict__.update()
