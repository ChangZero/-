import sys
n = int(input())
array = []
for _ in range(n):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    array.append([age, name])
array.sort(key= lambda x : x[0])
for i in array:
    print(i[0], i[1])