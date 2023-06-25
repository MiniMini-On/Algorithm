def solution(name, yearning, photo):
    answer = []
    name_dict = {}
    for n, y in zip(name, yearning):
        name_dict[n] = y
   
    
    for p in photo:
        score = 0
        for el in p:
            try:
                score += name_dict[el]
            except:
                pass
        answer.append(score)
             
        
    return answer