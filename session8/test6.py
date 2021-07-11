def get_num(n, c):
    if len(n) < 1:
        return

    for i in range(len(n)):
        t = n.copy()
        del t[i]
        if sum(t) < c:
            print(sum(t))
            return

    del n[0]
    get_num(n)


if __name__ == '__main__':
    first = [int(n) for n in input().split()]

    nums = []
    for _ in range(first[1]):
        nums.append(int(input()))

    get_num(sorted(nums), first[0])