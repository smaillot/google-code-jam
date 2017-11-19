import numpy as np
import fileinput
f = fileinput.input()

def is_composed(col):
    d = {}
    d['R'] = [1, 0, 0]
    d['O'] = [1, 1, 0]
    d['Y'] = [0, 1, 0]
    d['G'] = [0, 1, 1]
    d['B'] = [0, 0, 1]
    d['V'] = [1, 0, 1]
    return d[col] 

def can_be_neighbors(col1, col2):
    return np.sum([is_composed(col1)[i] * is_composed(col2)[i] for i in range(3)]) == 0

def get_color(unicorn):
    if np.sum(unicorn) == 1:
        d = {}
        d[0]='R'
        d[1]='O'
        d[2]='Y'
        d[3]='G'
        d[4]='B'
        d[5]='V'
        return d[unicorn.index(1)]

def get_neighbors(stable, pos):
    neighbors = []
    if pos != 0:
        neighbors.append(stable[pos-1])
    if pos != len(stable - 1):
        neighbors.append(stable[pos+1])
    if pos == -1:
        return stable[0]
    if pos == len(stable):
        return stable[-1]
    return neighbors

def add_unicorns_old(current_stalls, unicorns, N):
    #print('step : ' + current_stalls)
    if len(current_stalls) == N:
        return current_stalls
    if current_stalls != 'IMPOSSIBLE':
        if np.sum(unicorns) == 0:
            return current_stalls
        elif np.sum(unicorns) == 1:
            last_uni = get_color(unicorns)
            if len(current_stalls) == 0:
                return last_uni
            neighbor = current_stalls[-1]
            if can_be_neighbors(neighbor, last_uni):
                return current_stalls + last_uni
            else:
                return 'IMPOSSIBLE'
        else:
            #print('step : ' + current_stalls)
            for c in range(6):
                if unicorns[c] != 0:
                    new = [u for u in unicorns]
                    new[c] -= 1
                    single = [0]*6
                    single[c] = 1
                    #print('\tTrying ' + get_color(single))
                    #print('new ' + str(new))
                    final_res = add_unicorns(add_unicorns(current_stalls, single, N), new, N)
                    if final_res != 'IMPOSSIBLE':
                        if can_be_neighbors(final_res[0], final_res[-1]):
                            return final_res
    return 'IMPOSSIBLE'
    
def add_unicorns(unicorns, N):
    RYB = [unicorns[::2]]
    min_RYB = np.min(RYB)
    min_col_RYB = RYB.index(min_RYB)
    res = []
    others = [i for i in unicorns]
    others[min_col_RYB] = 0
    d = {}
    d[0] = 'R'
    d[1] = 'Y'
    d[2] = 'B'
    for i in range(min_RYB):
        if np.sum(others) != 0
            res.append(d[min_col_RYB])
            for j in range(3):
                if others[j] != 0:
                    res.append(d[j])
                    others[j] -= 1
        else:
            break
    
T = int(f.readline().rstrip('\n'))
for case in range(T):
    line = f.readline().rstrip('\n').split()
    N = int(line[0])
    unicorns = [int(i) for i in line[1:]]
    # function
    res = add_unicorns('', unicorns, N)
    print('Case #' + str(1+case) + ': ' + str(res))