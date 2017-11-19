import fileinput
f = fileinput.input()
def compute(N, K):
    N = [N]
    mini = 0
    maxi = 0
    for _ in range(K):
        largest = N.pop()
        mini = (largest - 1) // 2
        maxi = largest - 1 - mini
        if mini > 0:
            N.append(mini)
        if maxi > 0:
            N.append(maxi)
        while len(N) < 2:
            N.append(0)
        N.sort()
        print(N)
    return (mini, maxi)

T = int(f.readline().rstrip('\n'))
for t in range(T):
    entry = f.readline().rstrip('\n').split()
    m, M = compute(int(entry[0]), int(entry[1]))
    print('Case #' + str(t+1) + ': ' + str(M) + ' ' + str(m))