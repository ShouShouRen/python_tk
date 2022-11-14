import random
check = [0]*101
score = [[0]*8 for i in range(5)]
count = 0
stu = 0
for i in range(5):
    while count < 6:
        x = random.randint(60,100)
        if check[x]==0:
            score[stu][count]=x
            count+=1
            check[x]=1
    count = 0
    check = [0]*101
    stu+=1
for i in range(5):
    for j in range(6):
        print(score[i][j],end = ' ')
    print()