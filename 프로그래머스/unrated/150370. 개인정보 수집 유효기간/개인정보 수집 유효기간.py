from datetime import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):    
    term_dic = {}
    for term in terms:
        term_list= term.split(' ')
        term_dic[term_list[0]] = int(term_list[1])
    today = ''.join(today.split('.'))
    print(today)
    term_dic_keys = list(term_dic.keys())
    print(term_dic)  

    
    
    answer = []
    index = 1
    
    for p in privacies:
        privacy = p[:10].replace(".","")
        key = p[-1]
   
        due = term_dic[key]
        # print(int(due))
        end = datetime.strptime(today, "%Y%m%d")
        start = datetime.strptime(privacy, "%Y%m%d")
        delta = relativedelta(end, start)
        
        delta_months = delta.months + (delta.years*12)
        delta_days = delta.days  
        
        if delta_months >= int(due):
            # print(index)
            answer.append(index)
        index += 1
        
    
    
#     print(delta_months)
#     print(delta_days)
#     print(term_dic)
    
    
    return answer