def u(n):
    u = 2
    for i in range(1, n):
        u = 3 * u - 1
    return u

n = int(input("n = "))
print(u(n))