from collections import deque
import sys
f = sys.stdin.readline

n = int(f())
m = int(f())


#인접 리스트 graph = [[인접지,시간],...]
graph = [[] for _ in range(n+1)]

rev_graph = [[] for _ in range(n+1)]



#해당 도착지까지 루트 중 가장 오래 걸린 시간
time = [0]*(n+1)

# 진입차수 리스트 (인접 리스트에 -1을 하고 0가 되면 q에 넣는다)
indegree = [0]*(n+1)    

for _ in range(m):
    s, a, t = map(int, f().split())
    graph[s].append([a,t])
    indegree[a] += 1
    
    rev_graph[a].append([s,t])


s, a = map(int, f().split())

def bfs(start):
    q = deque()
    q.append(start)
    

    
    
    while q:

        now = q.popleft()
        
        for i in graph[now]:
            
            indegree[i[0]] -= 1
            
            if indegree[i[0]] == 0:
                q.append(i[0])
            
            now_time = time[now] +i[1]
            
            # 가장 오래 걸리는 시간을 구하기 위해 비교함
            if now_time > time[i[0]]:
                
                time[i[0]] = now_time
                
            
                
                

bfs(s)  

max_time = time[a]
print(max_time, end='\n')

count = 0

#시간이 최대가 되도록 역추적
def rev_dfs(end):
    v = [False]*(n+1)
    q = deque()
    q.append(end)
    v[end] = True
    global count 

    while q:
        now = q.popleft()
        for i in rev_graph[now]:
            if time[i[0]] + i[1] == time[now]:
                count += 1
                if not v[i[0]]:
                    v[i[0]] = True
                    q.append(i[0])
                

rev_dfs(a)

print(count, end='\n')




   
    