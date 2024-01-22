from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    related_list = [[] for _ in range(len(words)+2)]
    dq = deque(words)
    dq.appendleft(target)
    dq.appendleft(begin)
    print(dq)
    index = 0
    for word1 in dq:
        for word2 in dq:
            if word1 != word2:
                diff = 0
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        diff += 1
                if diff == 1:
                    related_list[index].append(word2)
                    
        index+=1
                    

    visited = [0] *(len(words)+2)
    
    distance = [0] *(len(words)+2)
 

    temp_dq = deque([begin])
    visited[0] = 1
    while temp_dq:
        now_node = temp_dq.popleft()
        print(now_node)
        now_node = dq.index(now_node)
        for node in related_list[now_node]:
            node_index = dq.index(node)
            if visited[node_index] ==0:
                temp_dq.append(node)
                distance[node_index] =distance[now_node]+1
                if node == target:
                    answer = distance[node_index]
                    return answer
                
                
        
     

    