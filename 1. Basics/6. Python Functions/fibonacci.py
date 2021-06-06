"""
Fibonacci Sequence

Fibonacci sequence is sequence where each number is the sum of 2 preceding one.
For example: 0, 1, 1, 2, 3, 5, 8, 13... so on
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(10))
