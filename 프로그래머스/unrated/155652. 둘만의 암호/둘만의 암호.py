from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

def solution(s, skip, index):
    answer = ''
    
    alphabet = {}
    key = 0
    
    for a in alphabet_list:
        if a not in skip:
            alphabet[key] = a
            key += 1
            
    print(alphabet)
            
            
    
    for ss in s:
        
        k = [k for k, v in alphabet.items() if v == ss][0]
        if k+index > len(alphabet)-1:
            answer += alphabet[(k+index) % len(alphabet)]

        else:
            answer += alphabet[k+index]
     

    return answer