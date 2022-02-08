line1 = input()
line2 = input()
cond = line1.split(" ")
num = line2.split(" ")
minvsnum = 300000
minsum = 0
if len(num) != int(cond[0]):
    print("잘못입력했습니다.")

for i in range(int(cond[0])):
    sum = int(num[i])
    for j in range(i+1,int(cond[0])):
        sum = int(num[i]) + int(num[j])
        for k in range(j+1,int(cond[0])):
            sum = int(num[i]) + int(num[j]) + int(num[k])
            if int(cond[1]) >= sum:
                vsnum = int(cond[1]) - sum
                if minvsnum > vsnum:
                    minvsnum = vsnum
                    minsum = sum

    
print(minsum)