def get_num(n):
    if n == 1:
        return n
    print(get_num(n-1))
    return n


if __name__ == '__main__':
    N = int(input())

    print(get_num(N))


