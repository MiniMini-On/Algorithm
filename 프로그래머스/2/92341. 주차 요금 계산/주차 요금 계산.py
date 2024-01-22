import math
def solution(fees, records):
    answer = []
    summary = {}
    summary_fee = {}
    temp = {}
    basal_min=fees[0]
    basal_fee=fees[1]
    unit_time=fees[2]
    unit_fee=fees[3]
    
    for car in records:
        car = car.split(' ')
        time = int(car[0].split(':')[0])*60 + int(car[0].split(':')[1])
        car_num = car[1]
        type = car[2]
        if type == 'IN':
            temp[car_num] = time
        else:
            if car_num in summary:
                
                summary[car_num] = summary[car_num] - temp[car_num] + time
            else:
                summary[car_num] = -temp[car_num] + time
            del temp[car_num]
            
    if temp:
        for car_num in temp.keys():
            time = 23*60 +59
            if car_num in summary:
                
                summary[car_num] = summary[car_num] - temp[car_num] + time
            else:
                summary[car_num] = -temp[car_num] + time
    
            
    print(summary)
    
    for k,v in summary.items():
        if v - basal_min <= 0:
            summary_fee[k] = basal_fee
        else:
            summary_fee[k] = basal_fee + math.ceil((v - basal_min)/unit_time)*unit_fee
    
    dic = dict(sorted(summary_fee.items()))
 
            
    answer =  list(dic.values())
            
    
    return answer