import sys


f = sys.stdin.readline

n, m = map(int, f().split())

l = list(map(int, f().split()))
    

sum_l = [0]
sum = 0
for i in l:
    sum += i
    sum_l.append(sum)
    

    
for _ in range(m):
    i, j = map(int, f().split()) 
    print(sum_l[j] - sum_l[i-1])
    

    
    

    