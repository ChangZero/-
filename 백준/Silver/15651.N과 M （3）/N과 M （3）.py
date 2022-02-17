from itertools import product

n, m = map(int, input().split())
num = []
for i in range(1,(n+1)):
    num.append(str(i))
    
for i in product(num, repeat=m):
    print(" ".join(i))