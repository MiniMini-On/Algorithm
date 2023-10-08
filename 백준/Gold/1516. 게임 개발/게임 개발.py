from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  
self = [0] * (N + 1)  

for i in range(1, N + 1):
    inputs = list(map(int, input().split()))
    self[i] = (inputs[0]) 
    index = 1
    while True: 
        temp = inputs[index]
        index += 1
        if temp == -1:
            break
        A[temp].append(i)
        indegree[i] += 1 

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (N + 1)
while queue:  
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + self[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(result[i] + self[i])