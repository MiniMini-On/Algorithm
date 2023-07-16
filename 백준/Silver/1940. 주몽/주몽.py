import sys

f = sys.stdin.readline

m = int(f().strip())
n = int(f().strip())
nums = list(map(int, f().split()))

#오름차순 정렬
nums.sort()

a = 0
b = 1


answer = 0

while b > a and b < m:
    
    sum = nums[a] + nums[b]
   
    if sum == n:
        answer += 1
        a += 1
        b= a+1
        
    elif sum > n:
        a += 1
        b= a+1
    else:
        b += 1
        if b >= m:
            a += 1
            b= a+1
       
        
print(answer)
        
        

