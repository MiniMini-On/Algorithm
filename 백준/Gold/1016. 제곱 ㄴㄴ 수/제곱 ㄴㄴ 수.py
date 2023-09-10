import math


min, max = map(int, input().split())

check = [False] * (max - min + 1)

for i in range(2, int(math.sqrt(max) + 1)):
    square = i * i
    start_index = math.ceil(min / square)
	
    for j in range(start_index, int(max / square) + 1):	
        check[int((j * square) - min)] = True
        
count = 0

for i in range(0, max - min + 1):
    if not check[i]:
        count += 1
        
print(count)