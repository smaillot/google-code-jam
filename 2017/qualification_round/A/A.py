import fileinput
f = fileinput.input()

def turn(S, K, p):
    T = [0]*len(S)
    for i in range(len(S)):
        if i >= p and i < p + K:
            T[i] = str(1 - int(S[i]))
        else:
            T[i] = S[i]
    return T

def turns(S, K):
    t = []
    for k in range(len(S)-K+1):
        T = turn(S, K, k)
        if not T in t:
            t.append(T)
    return t

def count(S, K):
    out = 0
    t = [S]
    if not ['1']*len(S) in t:
        for i in range(200):
            for s in t:
                T = turns(s, K)
                for it in T:
                    if it == ['1']*8:
                    if not it in t:
                        t.append(it)
            if ['1']*len(S) in t:
                print(t)
                out = i + 1
                break
    return out

T = int(f.readline().rstrip('\n'))
for _ in range(T):
    line = f.readline().rstrip('\n').split()
    print(count(line[0].replace('+','1').replace('-','0'), int(line[1])))
