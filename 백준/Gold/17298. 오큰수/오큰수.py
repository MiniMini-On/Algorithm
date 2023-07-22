import sys
from collections import deque


f = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))

answer = [0]*n

q = deque()

q.append(0)

for i in range(1,n):
    
    if list[i] > list[q[-1]]:
        while q and list[i] > list[q[-1]]:
            answer[q.pop()]=list[i]
        q.append(i)
    
    else:
        q.append(i)
        
        
while q:
    
    answer[q.pop()]=-1
    
for a in answer:
    print(a, end=' ')
            
    