# 가장 많이 신뢰받는 컴퓨터 찾기 

from collections import deque
import sys
f = sys.stdin.readline

n, m = map(int, f().split())

graph = [[] for _ in range(n+1)]



#신뢰받은 컴퓨터 수
num = [0] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)
    
def bfs(start):
    # 노드 방문 여부
    v = [False] * (n+1)
    
    q = deque()
    q.append(start)
    
    v[start] = True
    

    while q:
        now = q.popleft()
        for computer in graph[now]:
            if v[computer] == False:
               
                v[computer] = True
                num[computer] += 1
                q.append(computer)
            
             
for i in range(n):
    bfs(i+1)


max = max(num)

 

for index, i in enumerate(num):
    if i == max:
        print(index, end=' ')

