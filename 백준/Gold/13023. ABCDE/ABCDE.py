import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)


n, m = map(int,input().split())

visited = [False] * n
relation = [[] for _ in range(n)]


for _ in range(m):
    a, b = map(int,input().split())
    
    relation[a].append(b)
    relation[b].append(a) 
    
five = False           


def DFS(f, depth):
    
    global five
    
    visited[f] = True
    
    if depth == 5:
        five = True 
        return
    
    else:
        for i in relation[f]:
            if not visited[i]: #자기자신은 친구 X
                DFS(i, depth+1)
                
    visited[f] = False
    
for i in range(n):
    DFS(i, 1)
    if five:
        break
if five:
    print(1)
else:
    print(0)
        
    
    
    
    
                    
                    

                
                
                
            
    