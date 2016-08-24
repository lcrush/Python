terms = int(input("What number in Fibonocci due you want: "))

fib = []
fib.append(1)
fib.append(1)

for i in range(2, terms):
    fib.append(fib[i - 1] + fib[i - 2])
    
print(fib[terms - 1])

#----------------------------------------------------------

def fib(a):
    if a == 0 or a == 1:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)
    
print(fib(terms - 1))