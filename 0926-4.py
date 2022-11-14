import random
while True:
    for i in range(1, 7):
        randNum = random.randint(1, 36)
        print(randNum, end='    ')
    print()
    again = eval(input("continue: 1 or quit: 0 ---->"))
    if again == 0:
        break
print("Over")
