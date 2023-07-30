import sys
input = sys.stdin.readline


n = int(input())
m = list(map(int, input().split()))

m.sort()

now = 0
sum = 0

for i in range(n+1):
    for j in range(now):
       
        sum+=m[j]
    now+=1
    
print(sum)
        
    
    



