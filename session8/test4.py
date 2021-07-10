def get_num(n):
    if len(n) < 1:
        return

    for i in range(len(n)-1, 0, -1):
        t = n.copy()
        del t[i]
        print(t)

    del n[-1]
    get_num(n)


if __name__ == '__main__':
    N = int(input())

    for i in range(N):
        value = [n for n in range(i+1, N+1)]
        print(value)
        get_num(value)
