import sys
import math


input = sys.stdin.readline

s, e = map(int, input().split())

list = [i for i in range(e+1)]



now = 2
for i in range(2,e+1):
    
    if i > math.sqrt(e):
     
        break
    if list[i] != 0:
        now = i
        

    for j in range(now+now, e+1 ,now):

        if j == 0:
            continue 
        else:
            list[j] = 0

            
for i in list[s:e+1]:
    if i != 0 and i != 1:
        print(i)

        


