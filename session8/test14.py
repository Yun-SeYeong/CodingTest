def get_num(nums, n):
    if n <= 1:
        return [[n] for n in nums]

    nums1 = get_num(nums, n-1)
    print(nums1)
    result = []
    for i in range(len(nums1)):
        for j in range(n-1, len(nums)):
            if nums[j] not in nums1[i] and nums[j] > nums1[i][-1]:
                t = nums1[i].copy()
                t.append(nums[j])
                result.append(t)

    return result


if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]

    result = get_num([i+1 for i in range(first[0])], first[1])
    print(result)
    for r in result:
        print(" ".join(str(s) for s in r))

    print(len(result))