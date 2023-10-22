import sys
input = sys.stdin.readline
from queue import PriorityQueue

n, e = map(int, input().split())
start = int(input())

distance = [sys.maxsize] * (n+1)
visited = [False] * (n+1)

myList = [[] for _ in range(n+1)]

for _ in range(e):
    x, y, d = map(int, input().split())
    myList[x].append((d, y))
    
q = PriorityQueue()

q.put((0, start))
distance[start] = 0

while q.qsize() > 0:
    current = q.get()
    current_n = current[1]
    
    if visited[current_n]:
        continue
        
    visited[current_n] = True
    for l in myList[current_n]:
        if distance[l[1]] > current[0] + l[0]:
            distance[l[1]] = current[0] + l[0]
            q.put((current[0] + l[0],l[1]))
            
for i in range(1, n+1):
    if visited[i]:
        print(distance[i]) 
    else:
        print('INF')
        
        
        
