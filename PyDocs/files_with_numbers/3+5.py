def threeandfive(num):
    dasum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            dasum += i
    return dasum


print(threeandfive(1000))
