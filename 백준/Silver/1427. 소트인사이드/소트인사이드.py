import sys

print = sys.stdout.write

N = list(map(int, input()))
N.sort(reverse=True)


for i in range(len(N)):
    print(str(N[i]))