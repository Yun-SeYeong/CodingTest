def fac(n):
    if n <= 1:
        return n

    return n * fac(n-1)


def c(n, r):
    return fac(n) / (fac(n - r) * fac(r))


def c2(n, r):
    return int(c(n-1, r-1) + c(n-1, r))


if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]

    print(c2(first[0], first[1]))
