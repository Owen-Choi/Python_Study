def makeDict(K, V):
    D = {K[0]: V[0]}
    if(len(K) != len(V)):
        return

    for i in range(1, len(K)):
        D[K[i]] = V[i]
    return D

keys = ('Korean', 'Mathematics', 'English')
values = (90.3, 85.5, 92.7)
print(makeDict(keys, values))
