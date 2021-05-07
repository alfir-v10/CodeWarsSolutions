"""
The Fibonacci numbers are the numbers in the following integer sequence (Fn):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
such as
F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
F(n) * F(n+1) = prod.
Your function productFib takes an integer (prod) and returns an array:
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.
If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(m) being the smallest one such as F(m) * F(m+1) > prod.
"""


def power(x, n, I, mult):
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = power(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]


def matrix_multiply(A, B):
    bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in bt] for row_a in A]


def fib(n):
    f = power([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return f[0][1]


def product_fib(prod):
    if prod == 0:
        return [0, 1, True]
    elif prod == 1:
        return [1, 1, True]
    elif prod == 2:
        return [1, 2, True]
    elif prod == 3:
        return [2, 3, False]
    for i in range(1, prod):
        if fib(i) * fib(i + 1) > prod:
            return [int(fib(i)), int(fib(i + 1)), False]
        elif fib(i) * fib(i + 1) == prod:
            return [int(fib(i)), int(fib(i + 1)), True]

