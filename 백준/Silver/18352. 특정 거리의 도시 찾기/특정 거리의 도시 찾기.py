from collections import deque
import sys

# N과 M이 1000이상이기 때문에 dfs보다는 bfs가 적합

f = sys.stdin.readline

n, m, k, x = map(int, f().split())

# 인접 그래프 생성
graph = [[] for _ in range(n+1)]

# 방문 기록
v = [False] * (n+1)

# 거리
d = [0] * (n+1)

for _ in range(m):
    s, a = map(int, f().split())
    graph[s].append(a)



def bfs(start):
    q = deque()
    q.append(start)
    
    v[start] = True
    
    while q:
        now_node = q.popleft()

        for node in graph[now_node]:
            if v[node] == False:
                v[node] = True
                q.append(node)
                d[node] = d[now_node]+1
                
bfs(x)

answer = [node for node, value in enumerate(d) if value == k]


if len(answer) == 0:
    print(-1)
else:
    for a in answer:
        print(a, end='\n')
    
    

