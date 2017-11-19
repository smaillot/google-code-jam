if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    # loading inputs
    T = int(f.readline().rstrip('\n'))
    N = ['']*T
    for t in range(T):
        N[t] = f.readline().rstrip('\n')
    
    # Check if tidy
    def isTidy(n):
        tidy = True
        last = 0
        for i in str(n):
            if int(i) < last:
                tidy = False
                break
            else:
                last = int(i)
        return tidy
        
    # Find last call
    def reduce(n, i):
        n[i] = str(int(n[i]) - 1)
        for j in range(i+1, len(n)):
            n[j] = '9'
        return n
        
    def findLastTidy(n):
        k = list(str(n))
        i = 0
        while i < len(k)-1:
            if int(k[i]) > int(k[i+1]):
                k = reduce(k, i)
                i = 0
            else:
                i += 1
        return int(''.join(k))
        
    # Outputs
    for t in range(T):
        print('Case #' + str(t+1) + ': ' + str(findLastTidy(N[t])))