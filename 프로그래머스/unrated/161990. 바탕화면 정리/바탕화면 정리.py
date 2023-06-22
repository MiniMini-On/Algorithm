# 시간복잡도 O(n)

def solution(wallpaper):

    answer = [None,None,None,None]
    
    if len(wallpaper) == 1 and len(wallpaper[0]) == 1:
        return [0,0,1,1]
    
    for i, el in enumerate(wallpaper):
        if "#" in el:
            if answer[0] != None:
                answer[2] = i
            else:
                answer[0] = i
            for j, ell in enumerate(el):
                if ell == '#' :
                    if answer[1] == None:
                        answer[1] = j
                    elif answer[3] == None:
                        answer[3] = j
                    elif answer[1] > j:
                        answer[1] = j
                    elif answer[3] < j:
                        answer[3] = j
        
    try:    
        answer[2] +=1
    except:
        answer[2] = answer[0] +1
       
    try:    
        answer[3] +=1 
    except:
        answer[3] = answer[1] +1
        
    
   
    return answer