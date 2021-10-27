def foldl(f, z, l):
    print("z =", z, "| l =", l)
    if l == []:
        return z
    else:
        z = f(z, l.pop(0))
        return foldl(f, z, l)

def f1(x, y):
    print("f(" + str(x) + ", " + str(y) + ") = " + str(2 * x - y))
    return 2 * x - y
    
def f2(x, y):
    return x + y
    
def f3(x, y):
    return x * y

print(foldl(f1, 2, [1, 2, 3, 4, 5]))
print(foldl(f2, 0, [1, 2, 3, 4, 5]))
print(foldl(f3, 1, [1, 2, 3, 4, 5]))

def foldr(f, z, l):
    if l == []:
        return z
    else:
        e = l.pop(0)
        return f(e, foldr(f, z, l))


print(foldr(f1, 2, [1, 2, 3, 4, 5]))
print(foldr(f2, 0, [1, 2, 3, 4, 5]))
print(foldr(f3, 1, [1, 2, 3, 4, 5]))