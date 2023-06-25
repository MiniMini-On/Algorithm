def solution(n, m, section):
    answer = 0
    start = 0
    for s in section:
        if start == 0:
            start = s
        else:
            if s - start + 1 <= m:
                continue
            else:
                answer += 1
                start = s
    answer +=1
        
    return answer