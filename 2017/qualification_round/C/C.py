import fileinput
import sys
from time import time
f = fileinput.input()

def add(N, x):
    for i in range(len(N)):
        if N[i][0] == x:
            N[i][1] += 1
            return N
    N.append([x, 1])
    return N

def compute(n, k):
    N = [[n, 1]]
    mini = 0
    maxi = 0
    for _ in range(k):
        if N[-1][1] == 1:
            largest = N.pop()[0]
        else:
            largest = N[-1][0]
            N[-1][1] -= 1
        mini = (largest - 1) // 2
        maxi = largest - 1 - mini
        if mini > 0:
            add(N, mini)
        if maxi > 0:
            add(N, maxi)
        if len(N) < 1:
            N=add(N, 0)
        N.sort()
    return (mini, maxi)


start = time()
T = int(f.readline().rstrip('\n'))
for t in range(T):
    entry = f.readline().rstrip('\n').split()
    m, M = compute(int(entry[0]), int(entry[1]))
    print('Case #' + str(t+1) + ': ' + str(M) + ' ' + str(m))

print(time()-start, file=sys.stderr)