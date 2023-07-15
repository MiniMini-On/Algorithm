import sys


f = sys.stdin.readline

n, m = map(int, f().split())

list = list(map(int, f().split()))
sum = [0]
temp = 0

for i in list:
    temp += i
    sum.append(temp)
    
answer = 0

remain = [0]*m


for i in sum[1:]:
    result = i%m
    
    remain[result] += 1
    
    if result == 0:
        answer += 1
        


for i in range(m):
    if remain[i] > 0:
    
        p = remain[i]*(remain[i]-1)//2
        answer += p
    
    
            
            
print(answer)