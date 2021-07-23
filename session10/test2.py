def get_num(nums, target):
    if len(nums) <= 0:
        return 0

    print(nums)
    nums2 = []
    result = 0

    for num in nums:
        if num + 1 >= target:
            result += 1
        else:
            nums2.append(num+1)
        if num + 2 >= target:
            result += 1
        else:
            nums2.append(num+2)

    result += get_num(nums2, target)
    return result


if __name__ == '__main__':
    n = int(input())

    print(get_num([0], n))
