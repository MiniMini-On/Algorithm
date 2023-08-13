import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

root = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0


for _ in range(m):
    u, v = map(int, input().split())
    
    root[u].append(v)
    root[v].append(u)
    


def DFS(now):
    visited[now] = True
    for i in root[now]:
        if not visited[i]:
            DFS(i)
            
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)
        
print(count)
            

