# list.index('a') 형식으로 list에서 value를 통해 index를 알아내는 방식은 시간복잡도가 O(n^2) 으로 크다
# 따라서 dictionary({"a":index})를 사용하였다.
# 시간복잡도는 O(n) 정도로 추측된다

def solution(players, callings):
    players_dict = {}
  
    for i, player in enumerate(players):
        players_dict[player] = i              
   
    
    for call in callings:
        index = players_dict[call] 
        
        front_player = players[index-1]
        players[index] = front_player
        players[index-1] = call
        
        players_dict[call] = index-1
        players_dict[front_player] = index
        
    return players