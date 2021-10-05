from math import floor, sqrt
def EstPremier(n):
    estPremier = True
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return estPremier

print("3 ?", EstPremier(3))
print("22 ?", EstPremier(22))
print("71 ?", EstPremier(71))
print("14641 ?", EstPremier(14641))