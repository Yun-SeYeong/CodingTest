if __name__ == '__main__':
    N = int(input())

    nums = input().split(" ")

    result = []
    result.append(nums[0])
    for i in range(1, len(nums)):
        if int(nums[i - 1]) < int(nums[i]):
            result.append(nums[i])

    print(" ".join(result))