import sys
input = sys.stdin.readline


n, m = map(int, input().split())
list = list(map(int, input().split()))

list.sort()


    
print(list[m-1])