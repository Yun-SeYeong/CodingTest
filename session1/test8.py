if __name__ == '__main__':
    nums = input().split(" ")

    print(nums)

    inums = [int(n) for n in nums]

    print(inums)

    inums.sort(reverse=True)
    print(inums)

    min_len = 1

    for i in range(len(inums)):
