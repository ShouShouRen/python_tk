import random

check = [0]*49
number = [0]*6
count = 0
while count<6:
    x = random.randint(1,48)
    if check[x]==0:
        number[count]=x
        count+=1
for i in range(6):
    print(number[i],end=" ")
