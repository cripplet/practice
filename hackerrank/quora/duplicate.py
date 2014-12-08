import fileinput

import numpy as np
from collections import defaultdict
from json import loads

mat = defaultdict(int)
id = []

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	global mat, id
	q = int(args[0])
	d = int(args[1 + q])
	n = int(args[2 + q + d])
	id = []
	for l in args[1:1 + q]:
		id.append(loads(l)['question_key'])
	for l in args[2 + q:2 + q + d]:
		(src, tgt, related) = l.split()
		# +/-100
		score = int(related)
		mat[(src, tgt)] += score
		mat[(tgt, src)] += score
	tests = []
	for l in args[3 + q + d:]:
		tests.append(tuple(l.split()))
	t = np.ndarray(shape=(q, q))
	for i, u in enumerate(id):
		for j, v in enumerate(id):
			t[i, j] = t[j, i] = mat[u, v]
	(U, s, V) = np.linalg.svd(t, full_matrices=False)
	S = np.diag(s)
	y = np.dot(U, np.dot(S, V))
	np.allclose(t, y)
	mat = y
	t = { v:k for k, v in enumerate(id) }
	id = t
	return(tests)

def solve(args, verbose=False):
	global mat, id
	tests = proc_input(args)
	for (x, y) in tests:
		print x, y, int(round(mat[id[x], id[y]]))
	
def test():
	global mat, id
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	solve([ '3', '{"view_count": 773, "question_text": "Which is the most intelligent alien or alien species in fiction?", "context_topic": {"followers": 130960, "name": "Science Fiction (genre)"}, "topics": [{"followers": 48, "name": "Science Fiction Books"}, {"followers": 130960, "name": "Science Fiction (genre)"}, {"followers": 1182, "name": "Extraterrestrial Intelligence"}, {"followers": 50056, "name": "Extraterrestrial Life"}, {"followers": 3883, "name": "Science Fiction Movies"}], "follow_count": 9, "question_key": "AAEAAJ/qtRMKkzXyA0tvjyz5tPRWgYizvOkCr9Z9CdJ4cood", "age": 413}', '{"view_count": 3522, "question_text": "What is the best way to keep bookmarks?", "context_topic": {"followers": 513, "name": "Bookmarking"}, "topics": [{"followers": 1136, "name": "Pocket (app)"}, {"followers": 9, "name": "ReadItLater"}, {"followers": 1625, "name": "Pinboard"}, {"followers": 1275, "name": "Social Bookmarking"}, {"followers": 513, "name": "Bookmarking"}, {"followers": 5604, "name": "Delicious (web application)"}, {"followers": 4359, "name": "Instapaper"}, {"followers": 85, "name": "Web Bookmarks"}], "follow_count": 62, "question_key": "AAEAADJKxcVF6l23JZvf1Fz+QrKr35CTlMKayNnZebc8dQAY", "age": 1193}', '{"view_count": 390, "question_text": "What is best for online bookmarks?", "context_topic": null, "topics": [{"followers": 1275, "name": "Social Bookmarking"}, {"followers": 285, "name": "Social Bookmarking Websites"}, {"followers": 513, "name": "Bookmarking"}], "follow_count": 4, "question_key": "AAEAAO3FKYrsnYH9uKAOnnXfYrGGTVFA3uzHz+Vltm5Ssii3", "age": 1211}', '2', 'AAEAADJKxcVF6l23JZvf1Fz+QrKr35CTlMKayNnZebc8dQAY AAEAAO3FKYrsnYH9uKAOnnXfYrGGTVFA3uzHz+Vltm5Ssii3 1', 'AAEAADJKxcVF6l23JZvf1Fz+QrKr35CTlMKayNnZebc8dQAY AAEAAJ/qtRMKkzXyA0tvjyz5tPRWgYizvOkCr9Z9CdJ4cood 0', '1', 'AAEAAJ/qtRMKkzXyA0tvjyz5tPRWgYizvOkCr9Z9CdJ4cood AAEAAO3FKYrsnYH9uKAOnnXfYrGGTVFA3uzHz+Vltm5Ssii3' ])


if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
