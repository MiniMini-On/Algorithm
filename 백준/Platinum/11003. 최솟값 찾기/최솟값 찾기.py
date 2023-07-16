import sys
from collections import deque


f = sys.stdin.readline

n, m = map(int, f().split())

nums = list(map(int, f().split()))



q = deque()
q.append((0, nums[0]))
answer = [nums[0]]


for i in range(1, n):
  
    
    while q and nums[i] <= q[-1][1]:
        
        q.pop()
    q.append((i, nums[i]))
        
    if i - q[0][0]  >= m: 
        q.popleft()
        
    answer.append(q[0][1])

        
for i in answer:
    print(i, end=' ')       
        

    
    