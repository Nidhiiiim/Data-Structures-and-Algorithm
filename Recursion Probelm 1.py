# Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# Fibonacci Series
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))


# Sum of n numbers
def nsum(n):
    if n == 0:
        return 0
    return n + nsum(n - 1)


print(nsum(5))


