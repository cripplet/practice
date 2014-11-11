import fileinput

input = []

for line in fileinput.input():
	try:
		input.append(int(line))
	except ValueError:
		pass

def calc(x):
	r = ((x + 1) / 2)
	if x & 1:
		r *= -1
	return r

for x in input:
	print calc(x)
