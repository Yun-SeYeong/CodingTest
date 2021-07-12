def get_num(n):
    if n <= 1:
        return n

    return n * get_num(n-1)


if __name__ == '__main__':
    N = int(input())

    print(get_num(N))