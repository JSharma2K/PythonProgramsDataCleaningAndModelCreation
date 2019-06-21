def depth(P):
    hT = {}
    maxDepth = 0
    for i in range(len(P)):
        idepth = 1
        while (P[i] != -1):
            if hT[P[i]] != None:
                idepth += hT[P[i]]
                break
            else:
                idepth += 1
                i = P[i]
        hT[i] = idepth
        maxDepth = max (idepth, maxDepth)
    return maxDepth
print depth([-1, 0,0,0,2,2,5,6,6,8,8,8])
