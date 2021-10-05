def EstPair(liste):
    estPair = True
    for elem in liste:
        if elem % 2 == 1:
            estPair = False
            break
    return estPair

l1 = [2, 4, 6]
l2 = [2, 5, 6]
print(l1, "est pair ?", EstPair(l1))
print(l2, "est pair ?", EstPair(l2))