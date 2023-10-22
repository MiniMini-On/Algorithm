import sys
input = sys.stdin.readline

node, root = map(int, input().split())
edges = []
distance = [sys.maxsize] * (node+1)

for _ in range(root):
    s, e, r = map(int, input().split())
    edges.append((s, e, r))

distance[1] = 0

for _ in range(node-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

minus = False       
 
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        minus = True

if not minus:
    for i in range(2,node+1):
        if distance[i] == sys.maxsize:
            print(-1)
        else:
            print(distance[i])
    
else:
    print(-1)
