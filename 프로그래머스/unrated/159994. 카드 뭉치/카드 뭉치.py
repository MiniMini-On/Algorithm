def solution(cards1, cards2, goal):
    answer = 'Yes'
    for g in goal:
        
        if g == cards1[0]:
            cards1.pop(0)
            ##length가 0이 되지 않도록 한다
            cards1.append('메롱')
        
        elif g == cards2[0]:
            cards2.pop(0)
            ##length가 0이 되지 않도록 한다
            cards2.append('메롱')
            
        else:
            return 'No'
        
         
            
    return answer