import sys
import statistics

f = sys.stdin.readline

n = int(f())

m = list(map(int, f().split()))

max = max(m)

answer = statistics.mean(m) * 100/max

print(answer)