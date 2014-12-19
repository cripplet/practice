import math
class NumberGameAgain(object):
	def solve(self, k, forbid):
		n_unreach = 0
		for x in forbid:
			i = x
			proc = True
			while i > 1:
				i = i / 2
				if i in forbid:
					proc = False
			if proc:
				h_subtree = k - math.floor(math.log(x, 2))
				n_subtree = 2 ** h_subtree - 1
				n_unreach += n_subtree
		return 2 ** k - 2 - n_unreach

print(NumberGameAgain().solve(28, [ 373, 31260440, 97482257, 188776065, 185063003, 831, 4, 68263201, 26, 9, 737, 68650298, 235235276, 628, 6, 228047431, 749, 189364347, 146861366 ]))
print(NumberGameAgain().solve(21, [ 382020, 1445653, 31, 29, 300, 821043, 1608648, 938706, 993, 328, 303126, 803567, 1635671, 181113, 448, 9, 23992, 16, 128, 18 ]))
