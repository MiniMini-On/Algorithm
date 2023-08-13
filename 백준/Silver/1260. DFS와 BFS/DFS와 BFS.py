import sys
from collections import deque

input = sys.stdin.readline

sys.setrecursionlimit(10000)


n, m, start = map(int,input().split())

visited = [False] * (n+1)
connect = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int,input().split())
    
    connect[a].append(b)
    connect[b].append(a) 
    
for i in connect:
    i.sort()
    
           


def DFS(start):

    
    print(start, end=' ')
    
    visited[start] = True
    for i in connect[start]:
        if not visited[i]:
            DFS(i)
            
DFS(start)


visited = [False] * (n+1)
           
   
def BFS(start):

    q = deque()
    q.append(start)
    visited[start] = True
    
    
    while q:
        now = q.popleft()
        print(now, end=' ')
        
        for i in connect[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
print()           
BFS(start)


        
    
    
    
    
                    
                    

                
                
                
            
    