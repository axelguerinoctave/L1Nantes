def EstPair(liste):
    estPair = True
    print("input:", liste)
    for elem in liste:
        print("elem :", elem)
        if elem % 2 == 1:
            print("impair")
            estPair = False
            break
    return estPair

def EstPair2(liste):
    estPair = True
    for elem in liste:
        elem_estPair = (elem % 2 == 0)
        estPair = estPair and elem_estPair
        print("elem :", elem)
        print("elem pair ?", elem_estPair)
        print("list pair ?", estPair)
    return estPair 

l1 = [2, 4, 6]
l2 = [2, 5, 6]

print(l1, "est pair ?", EstPair(l1))
print(l2, "est pair ?", EstPair(l2))

print(l1, "est pair ?", EstPair2(l1))
print(l2, "est pair ?", EstPair2(l2))