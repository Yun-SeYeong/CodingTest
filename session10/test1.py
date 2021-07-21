def get_num(nums, n):
    if len(nums) <= 0:
        return 0
    result = 0

    nums2 = []
    for num in nums:
        if num < n:
            nums2.append(num + 1)
            nums2.append(num + 2)
        elif num == n:
            result += 1

    result += get_num(nums2, n)
    return result


if __name__ == '__main__':
    n = int(input())

    print(get_num([0], n))