import sys


def fact(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return n * fact(n-1)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(fact(n))
