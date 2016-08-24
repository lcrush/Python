import math
terms = int(input("How many terms: "))

pi = 0.0

for i, denom in enumerate(range(1, terms * 2, 2)):
#    print(i, i % 2, denom)
    if i % 2 == 0:
        pi = pi + (4/denom)
    else:
        pi = pi - (4/denom)
print(pi, math.pi)