import sys


def fib(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(fib(n))
