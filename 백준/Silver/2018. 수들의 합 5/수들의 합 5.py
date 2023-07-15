

n= int(input())

start = 1
end = 1
sum = 1

answer = 0

while start <= n and end <= n:
    
    if sum == n:
        answer += 1
        end += 1
        sum += end
        
    elif sum > n:
        sum -= start
        start += 1
        
    else:
        end += 1
        sum += end   
  
print(answer)
    
  
        
