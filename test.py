n = 1
d = 1
i = 0
f = 0
sum = 0
while i <= 2021:
    f = ((1 + n) * n) / 2
    f = 1/f
    i = i + 1
    n = n + 1
    sum = sum + f
    print(2*2021/sum)
