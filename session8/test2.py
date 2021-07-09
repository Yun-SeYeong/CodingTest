def get_num(n):
    if n < 1:
        return
    get_num(int(n/2))
    print(n % 2)


if __name__ == '__main__':
    N = int(input())
    get_num(N)