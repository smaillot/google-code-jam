import numpy as np
import fileinput
f = fileinput.input()

def time_to_reach(start, end, speed):
    return (end - start) / speed

def find_maximum_speed(D, H):
    slowest = -1
    slowest_end = -1
    if np.ndim(H) != 1:
        for i in range(len(H)):
            if slowest == -1:
                slowest = i
                slowest_end = time_to_reach(H[i, 0], D, H[i, 1])
            else:
                current = time_to_reach(H[i, 0], D, H[i, 1])
                if current > slowest_end:
                    slowest = i
                    slowest_end = current
        return D / slowest_end
    else:
        return D / time_to_reach(H[0], D, H[1])

T = int(f.readline().rstrip('\n'))
for case in range(T):
    line = f.readline().rstrip('\n').split()
    D = int(line[0])
    N = int(line[1])
    H = np.zeros((N,2))
    for i in range(N):
        horse = f.readline().rstrip('\n').split()
        H[i] = horse
    # functions
    res = find_maximum_speed(D, H)
    print('Case #' + str(1+case) + ': ' + str(res))