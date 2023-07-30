#루프를 몇번 돌았는지 알아내는 문제
import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append((int(input()), i))
Max = 0
sorted = sorted(A)


for i in range(N):
    if Max < sorted[i][1] - i:    # 정렬 전 index - 정렬 후 index 계산의 최댓값 저장하기
        Max = sorted[i][1] - i
print(Max + 1)
    



