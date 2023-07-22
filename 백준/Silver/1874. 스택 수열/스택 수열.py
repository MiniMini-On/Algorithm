import sys
from collections import deque


f = sys.stdin.readline

n = int(input())

q = deque()
for i in range(n):
    m = int(input())
    q.append(m)
    

answer = deque()
temp = [0]
i = 1
now = q.popleft()

while len(answer) < 2*n:
    if temp[-1] == now:
        answer.append('-')
        temp.pop()
        if q:
            now = q.popleft()
        
    else:
        if i <= now:
            answer.append('+')
            temp.append(i)
            i+=1
        else:
            answer.appendleft('NO')
            break

            


if answer[0] == 'NO':
    print('NO')
else:
    for a in answer:
        
        print(a)
        