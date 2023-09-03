import sys


input = sys.stdin.readline


n = int(input())
list = [[0]*2 for _ in range(n)]


count = 0

end = -1

for i in range(n):

    s, e = map(int, input().split())

    list[i][0] = e
    list[i][1] = s
    
list.sort()
    
for i in range(n):
    if end <= list[i][1]:
        end = list[i][0]
        count += 1
        
print(count)
    

    

