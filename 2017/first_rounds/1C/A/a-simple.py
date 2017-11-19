######################################
### begin template
###

from sys import stdin
from sys import stderr

N_CASE = 1

def getLine(f=int):
	t = tuple(f(i) for i in stdin.readline().split())
	if len(t) == 1:
		return t[0]
	else:
		return t

def getMat(rows, f=int):
	mat = []
	for _ in range(rows):
		mat.append(list(getLine(f)))
	return mat

def error(error_msg):
	print(error_msg, file=stderr)

def progress(x, y):
	error("Progress : {:.2f}% ({} / {})".format(100*x/y, x, y))

def output(answers):
	global N_CASE
	str_ans = str(answers)
	print("Case #{}: {}".format(N_CASE, str_ans))
	N_CASE += 1

###
### end template
######################################



######################################
### begin algorithm
###

import numpy as np

def compute_side_area(pc):
	(r, h) = tuple(pc)
	return 2 * np.pi * r * h

def compute_top_area(r):
	ans = np.pi * r ** 2
	# error('radius = ' + str(r) + ', area = ' + str(np.pi * r ** 2))
	return ans

def compute_area(pc):
	ans = compute_top_area(max(pc[:,0]))
	ans += np.sum(pc[:,1])
	return ans

T = getLine()
for _ in range(T):
	N, K = getLine()
	pc = np.array(getMat(N))
	pc = np.array([[p[0], compute_side_area(p)] for p in pc])
	pc = pc[pc[:,1].argsort()][::-1]
	error('Sides : \n' + str(pc))
	ans = pc[:K]
	error('Selected : \n' + str(ans))
	if max(pc[:,0]) > max(ans[:,0]):
		error('The largest pancake is not included')
		pc = pc[pc[:,0].argsort()][::-1]
		error('sorted by rad : \n' + str(pc))
		ans2 = np.concatenate((ans[:-1,:],np.array([pc[0, :]])))
		error('Solution with the largest pancake : \n' + str(ans2))
		area1 = compute_area(ans)
		area2 = compute_area(ans2)
		error('ans : ' + str(area1) + ', ans2 : ' + str(area2))
		ans = np.max((area1, area2))
	else:
		ans = compute_area(ans)
	output(ans)

###
### end algorithm
######################################

