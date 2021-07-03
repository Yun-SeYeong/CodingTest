if __name__ == '__main__':
    nums = input().split(" ")
    print(nums)

    inums = [int(n) for n in nums]

    inums_length = len(inums)
    for i in range(inums_length):
        for j in range(i+1, inums_length):
            if inums[i] > inums[j]:
                tmp = inums[i]
                inums[i] = inums[j]
                inums[j] = tmp
    print(inums)
    print(inums[0])

