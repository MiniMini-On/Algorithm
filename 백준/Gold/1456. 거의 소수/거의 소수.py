import sys
import math


input = sys.stdin.readline

s, e = map(int, input().split())

list = [i for i in range(int(math.sqrt(e))+1)]

count = 0



now = 2
for i in range(2,int(math.sqrt(e))+1):
    
    if i > math.sqrt(e):
     
        break
    if list[i] != 0:
        now = i
        

    for j in range(now+now, int(math.sqrt(e))+1 ,now):

        if j == 0:
            continue 
        else:
            list[j] = 0


            
for el in list:
    if el != 1 and el != 0:
        for i in range(2,1000000):
            if el ** i > e:
                break
            else:
                if el ** i >= s:
               
               
                    count += 1
        
print(count)

        


