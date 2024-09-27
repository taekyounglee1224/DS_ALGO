"큰 정수 곱셈하기"

a = 1234567812345678
b = 2345678923456789
threshold = 4

import math

def large_int_prod(u,v):

    n = max(len(str(u)), len(str(v)))

    if u == 0 or v == 0:
        return 0

    elif n <= threshold:
        return u * v

    else:
        m = math.floor(n/2)
        x, y = u // (10 ** m), u % (10 ** m)
        w, z = v // (10 ** m), v % (10 ** m)

        r = large_int_prod(x + y, w + z)
        p = large_int_prod(x, w)
        q = large_int_prod(y, z)

        return p * (10 ** (2 * m)) + (r - p - q) * (10 ** m) + q

print(large_int_prod(a, b))
print(a * b)

