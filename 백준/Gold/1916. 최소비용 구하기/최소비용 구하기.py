import sys
input = sys.stdin.readline
from queue import PriorityQueue

node = int(input()) 
root = int(input())  

cost = [sys.maxsize] * (node + 1)  
visited = [False] * (node + 1)        
myList = [[] for _ in range(node + 1)]  

for _ in range(root):
    s, e, w = map(int, input().split())  
    myList[s].append((w, e))

    
start, end = map(int, input().split())

q = PriorityQueue()

q.put((0, start))  
cost[start] = 0

while q.qsize() > 0:
    current = q.get()  
    current_v = current[1] 
    if visited[current_v]:
        continue
    visited[current_v] = True
    for tmp in myList[current_v]:
        next = tmp[1]
        value = tmp[0]
        if cost[next] > cost[current_v] + value:  # 최소 거리로 업데이트
            cost[next] = cost[current_v] + value
            q.put((cost[next], next))


print(cost[end])