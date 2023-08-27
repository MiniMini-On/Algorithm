import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
q = PriorityQueue()

ans = 0


for _ in range(n):  
    q.put(int(input())) 
    
while q.qsize() > 1:
    now1 = q.get()
    now2 = q.get()
    
    temp = now1 + now2
    ans += temp 
    q.put(temp) 
    
        
print(ans)
    
    