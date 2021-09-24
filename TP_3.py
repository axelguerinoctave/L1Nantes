def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def fact2(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

l = list(range(11))
for e in l:
    print(str(e) + "! = " + str(fact(e)))
    print(str(e) + "! = " + str(fact2(e)))