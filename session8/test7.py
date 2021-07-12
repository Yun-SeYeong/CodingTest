def get_num(n, m):
    if len(n) < 1:
        return 0

    # print(n)

    for i in range(len(n)):
        t = n.copy()
        del t[i]
        total = 0
        score = 0
        for j in t:
            total += j[1]
            score += j[0]
        # print("total: ", total)
        # print("score: ", score)
        # print("t: ", t)
        if total <= m:
            print(t)
            return total
        else:
            get_num(t, m)



if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]

    nums = []
    for _ in range(first[0]):
        nums.append([int(n) for n in input().split(" ")])

    print(nums)
    get_num(sorted(nums, key=lambda x: x[0]), first[1])