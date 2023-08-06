import sys
input = sys.stdin.readline

N = int(input())

# 10000이하의 숫자로만 이루어져 있으므로
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1
    
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)