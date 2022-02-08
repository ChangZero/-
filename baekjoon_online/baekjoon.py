import sys
num = sys.stdin.readline()
list = []
for i in num:
    list.append(i)
    
list.sort(reverse= True)
ans = ",".join(list)
print(''.join(list))