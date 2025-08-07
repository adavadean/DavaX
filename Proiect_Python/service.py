def pow_op(x: int, y: int) -> int:
    return x ** y

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def factorial(n: int) -> int:
    if n == 0:
        return 1
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
