import sys


input = sys.stdin.readline

answer = 0


strings = input().split('-')

first = strings[0].split('+')
for f in first:
    answer += int(f)

for s in strings[1:]:
    for n in s.split('+'):
        answer -= int(n)
        
print(answer)
        


