def prime(x, y):
    while x < y+1:
        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                yield x
        x += 1


for e in prime(1, 100):
    print(e, end=" ")
