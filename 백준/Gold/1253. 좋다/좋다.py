import sys

f = sys.stdin.readline

n = int(f().strip())

# 자연수가 아니라 정수임 !!
nums = list(map(int, f().split()))

nums.sort()
k = 0

i = 0
j = 0
answer = 0

for k in range(n):
    i = 0
    j = n-1
    
    while i<j :
        sum = nums[i] + nums[j]
        
        if sum == nums[k]:
            if i != k and j != k:
                answer += 1   
                break
            elif i == k:
                i += 1
                
            elif j == k:
                j -= 1
                
            
        elif sum < nums[k]:
            i += 1
            
        else:
            j -= 1
                
print(answer)
            
            
        
