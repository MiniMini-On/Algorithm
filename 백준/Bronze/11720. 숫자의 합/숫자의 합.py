import sys
f = sys.stdin.readline

n = int(f())
m = f().rstrip()

answer = 0
for i in m:
    answer += int(i)

print(answer)