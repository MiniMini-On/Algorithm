import sys
import heapq
input = sys.stdin.readline

n, r, k = map(int, input().split())
dist = [[sys.maxsize]*k for _ in range(n+1)]
myList = [[] for _ in range(n+1)]


for _ in range(r):
    s, e, d = map(int, input().split())
    myList[s].append((d, e))

pq = [(0, 1)]
dist[1][0] = 0

while pq:
    current = heapq.heappop(pq)
    current_node = current[1]
    current_dist = current[0]
    
    for l in myList[current_node]:
        if dist[l[1]][k-1] > current_dist + l[0]:
            dist[l[1]][k-1] = current_dist + l[0]
            dist[l[1]].sort()
            heapq.heappush(pq, [current_dist + l[0], l[1]])
            
for i in range(1, n+1):
    if dist[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(dist[i][k-1])
    