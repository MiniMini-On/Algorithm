import sys


f = sys.stdin.readline

n, m = map(int, f().split())

d = []




for _ in range(n):
    d.append(list(map(int, f().split())))



p_sum =[]

temp = []


for i in range(n+1):
    
    for j in range(n+1):
        if i == 0 or j == 0:
            temp.append(0)
           
        else:
            a = p_sum[i-1][j]+temp[j-1]-p_sum[i-1][j-1]+d[i-1][j-1]
            temp.append(a)
      
            
    p_sum.append(temp)
    temp = []

    
for _ in range(m):
    x1, y1, x2, y2 = map(int, f().split())
    
    answer = p_sum[x2][y2] - p_sum[x1-1][y2] - p_sum[x2][y1-1] + p_sum[x1-1][y1-1]
    print(answer)
    
    



            
    
    
    
    
    