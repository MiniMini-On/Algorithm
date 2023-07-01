from string import ascii_uppercase

alphabet_list = list(ascii_uppercase)

def solution(keymap, targets):
    answer = []
    
    ## alphabet_dict 생성
    alphabet_dict = {}
    for a in keymap:
        for index, key in enumerate(a):
            if key not in alphabet_dict:
                alphabet_dict[key] = index+1
            elif alphabet_dict[key] > index+1:
                alphabet_dict[key] = index+1
    
    for t in targets:
        temp = 0
        for tt in t:
            if tt in alphabet_dict:
                temp += alphabet_dict[tt]
            else:
                temp = -1
                break
        answer.append(temp)
             
    return answer