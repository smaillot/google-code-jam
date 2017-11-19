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
	print("Case #{}: {}".format(N_CASE, answers))
	N_CASE += 1

###
### end template
######################################



######################################
### begin algorithm
###

TIME_TABLE = [0]*(24*60)

def fill_tt(act, n):
	start, end = tuple(act)
	global TIME_TABLE
	for t in range(start, end):
		TIME_TABLE[t] = n

def count_empty():
	global TIME_TABLE
	return sum([i==0 for i in TIME_TABLE])

def increase(n):
	global TIME_TABLE
	inside = find_inside(n)
	if inside != []:
		TIME_TABLE[inside] = n
	else:
		TIME_TABLE[find_first_empty_neigh(n)] = n

def find_inside(n):
	last_pose = -1
	gap = False
	inside = []
	for t in range(len(TIME_TABLE)):
		if last_pose == -1:
			if TIME_TABLE[t] != 0:
				last_pose = t
		else:
			if gap == False:
				if TIME_TABLE[t] == 0:
					gap = True
			else:
				if TIME_TABLE[t] != 0 and TIME_TABLE[t] != n:
					inside = last_pose + 1
					return inside
				else:
					if TIME_TABLE[t] != 0 and TIME_TABLE[t] == n:
						gap = False
	if TIME_TABLE[-1] == n and TIME_TABLE[0] == 0:
		return 0
	else:
		return inside

def find_first_empty_neigh(n):
	global TIME_TABLE
	last_pose = -1
	for t in range(len(TIME_TABLE)):
		if TIME_TABLE[t] == 0 and TIME_TABLE[t-1] == n:
			return t
		if TIME_TABLE[t] == n and TIME_TABLE[t-1] == 0:
			return t-1

def count_trans():
	global TIME_TABLE
	last = -1
	ans = 0
	for t in range(len(TIME_TABLE)):
		if last != -1:
			if last != TIME_TABLE[t]:
				ans += 1
		last = TIME_TABLE[t]
	if TIME_TABLE[-1] != TIME_TABLE[0]:
		ans += 1
	return ans

T = getLine()
for _ in range(T):
	A1, A2 = getLine()
	TT1 = getMat(A1)
	TT2 = getMat(A2)
	for a in TT1:
		fill_tt(a, 2)
	for a in TT2:
		fill_tt(a, 1)

	n1 = sum([i==1 for i in TIME_TABLE])
	n2 = sum([i==2 for i in TIME_TABLE])
	while count_empty() > 0:
		to_increase = (1, 2)[n2 < n1]
		if to_increase == 1:
			increase(1)
			n1 += 1
		else:
			increase(2)
			n2 += 1

	ans = count_trans()
	output(ans)

###
### end algorithm
######################################

