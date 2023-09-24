from collections import deque

sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]
limit = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)] # A, B의 물의 양 저장
answer = [False] * 201

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    answer[limit[2]] = True
    while queue:
    
        
        now_Node = queue.popleft()
        A = now_Node[0]
        B = now_Node[1]
        C = limit[2] - A - B  
        
        for k in range(6):  
            next = [A, B, C]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0
            if next[receiver[k]] > limit[receiver[k]]:  
      
                next[sender[k]] = next[receiver[k]] - limit[receiver[k]]
                next[receiver[k]] = limit[receiver[k]] 
                 
            if not visited[next[0]][next[1]]: 
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                
                if next[0] == 0:  
                    answer[next[2]] = True

BFS()
for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')