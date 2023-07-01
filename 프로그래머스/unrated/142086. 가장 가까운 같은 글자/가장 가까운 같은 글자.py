def solution(s):
    dict = {}
    answer = []
    
    for index, ss in enumerate(s):
        if ss not in dict:
            answer.append(-1)
            dict[ss] = index
        else:
            answer.append(index - dict[ss])
            dict[ss] = index
            
            
    return answer