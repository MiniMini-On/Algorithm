N, M = map(int, input().split())
true_p = list(map(int, input().split()))  
del true_p[0]

result = 0
party = [[] for _ in range(M)]
parent = [0] * (N + 1)


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(M):
    party[i] = list(map(int, input().split())) 
    del party[i][0]

for i in range(N + 1):  
    parent[i] = i

for i in range(M):  
    first_p = party[i][0]
    for j in range(1, len(party[i])):
        union(first_p, party[i][j])

for i in range(M):
    isPossible = True
    first_p = party[i][0]
    for p in true_p:
        if find(first_p) == find(p):
            isPossible = False
            break
    if isPossible:
        result += 1  
        
print(result)