a = eval(input("input A:"))
b = eval(input("input B:"))
sum = 0
for i in range(a, b+1):
    if i % 2 == 0:
        sum += i
print("%d 到 %d 的偶數和 %d" % (a, b, sum))
