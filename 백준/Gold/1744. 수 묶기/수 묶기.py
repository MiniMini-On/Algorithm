import sys
from queue import PriorityQueue

input = sys.stdin.readline


n = int(input())
q_p = PriorityQueue()
q_m = PriorityQueue()

zero = 0
one = 0

ans = 0


for _ in range(n):  
    temp = int(input())
    if temp == 1:
        one += 1
    elif temp == 0:
        zero += 1
    elif temp > 1:
        q_p.put(temp*-1)
    else:
        q_m.put(temp)


    
while not q_p.empty():

    if q_p.qsize() == 1:
        ans += q_p.get()*-1
    else:
        now1 = q_p.get()*-1
        now2 = q_p.get()*-1
        
        temp = now1 * now2
        ans += temp 
        
while not q_m.empty():

    
    if q_m.qsize() == 1:
        if zero:
            q_m.get()
            
        else:    
            ans += q_m.get()
    else:
        now1 = q_m.get()
        now2 = q_m.get()
        
        temp = now1 * now2
        ans += temp 
      
ans += one 
        
print(ans)
    
    