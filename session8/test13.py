def get_pascal_num(nums, n):
    if n <= 1:
        return nums

    nums2 = get_pascal_num(nums, n-1)
    result = []
    for i in range(len(nums2)-1):
        result.append(nums2[i] + nums2[i+1])

    return result


def get_num(nums, n):
    if n <= 1:
        return [[n] for n in nums]

    nums2 = get_num(nums, n-1)

    result = []
    for num2 in nums2:
        for num in nums:
            if num not in num2:
                t = num2.copy()
                t.append(num)
                result.append(t)

    return result


if __name__ == '__main__':
    first = [int(n) for n in input().split()]
    nums_list = get_num([i+1 for i in range(first[0])], first[0])
    for nums in nums_list:
        if get_pascal_num(nums, first[0])[0] == first[1]:
            print(" ".join([str(s) for s in nums]))
            break
