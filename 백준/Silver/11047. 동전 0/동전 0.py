import sys

input = sys.stdin.readline

n, k = map(int, input().split())
A = []

ans = 0


for _ in range(n):  
    A.append(int(input()))   
    
for _ in range(n):
    now = A.pop()
    
    if now <= k:
        ans += k//now
        k = k%now
        if k == 0:
            break
        
print(ans)
    
    