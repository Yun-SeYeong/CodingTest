def get_nums(n, n2):
    if len(n) <= 2:
        return

    for i in range(len(n)):
        t = n.copy()
        t2 = n2.copy()
        t2.append(t[i])
        del t[i]

        print("n: ", t)
        print("n2: ", t2)
        if sum(t) == sum(t2):
            print("YES")
            return

    n2.append(n[0])

    get_nums(t, t2)


if __name__ == '__main__':
    N = int(input())
    nums = [int(n) for n in input().split()]

    get_nums(nums, [])