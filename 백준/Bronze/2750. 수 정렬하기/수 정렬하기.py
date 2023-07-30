import sys
from queue import PriorityQueue
input = sys.stdin.readline



n = int(input())
m = []

for _ in range(n):
    m.append(int(input()))
    
m.sort()
    
for i in m:
    print(i, end='\n')