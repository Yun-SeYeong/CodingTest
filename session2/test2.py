if __name__ == '__main__':
    N = input()
    nums = input().split(" ")

    result = 1
    max_height = int(nums[0])

    for i in range(1, len(nums)):
        if max_height < int(nums[i]):
            max_height = int(nums[i])
            result += 1

    print(result)