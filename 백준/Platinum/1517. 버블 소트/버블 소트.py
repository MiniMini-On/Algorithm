import sys
input = sys.stdin.readline

result = 0

def merge_sort(s, e):
    global result
    
    if e - s < 1: return
    m = int(s + (e - s) / 2) # 반띵
    merge_sort(s, m) # 반의 왼쪽
    merge_sort(m + 1, e) # 반의 오른쪽
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result += (index2 - k)
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:  #왼쪽 정리
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:  #오른쪽 정리
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
tmp = [0] * int(N + 1)

    
merge_sort(1, N)

print(result)
        
    
    



