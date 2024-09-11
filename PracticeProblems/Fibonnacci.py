def fibo_1(n):      #Recursive Method
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibo_1(n-2) + fibo_1(n-1)


def fibo_2(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    a,b = 0,1
    for i in range(2, n+1):
        a,b = b,a+b

    return b


for i in range(0,10):
    print(f'{i:2d} {fibo_1(i):6d}')

print()

for i in range(0,10):
    print(f'{i:2d} {fibo_2(i):6d}')


