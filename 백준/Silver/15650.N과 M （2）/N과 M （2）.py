from itertools import combinations

n, m = map(int, input().split())
num = []
for i in range(1,(n+1)):
    num.append(str(i))
    
array = list(combinations(num,m))
for i in array:
    print(" ".join(i))
