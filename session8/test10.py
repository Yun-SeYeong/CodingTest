def get_num(nums, n):
    if n < 2:
        result1 = []
        result2 = []
        for i in range(len(nums)):
            t = nums.copy()
            result1.append([t[i]])
            del t[i]
            result2.append(t)

        return result1, result2

    result1 = []
    result2 = []
    r1, r2 = get_num(nums, n - 1)
    for i in range(len(r1)):
        for j in range(len(r2[i])):
            t1 = r1[i].copy()
            t2 = r2[i].copy()
            t1.append(t2[j])
            del t2[j]
            result1.append(t1)
            result2.append(t2)

    return result1, result2


if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]
    second = [int(n) for n in input().split(" ")]

    result = get_num(second, first[1])[0]
    for nums in result:
        print(" ".join([str(i) for i in nums]))

    print(str(len(result)))
