if __name__ == '__main__':
    nums = input().split(" ")
    print(nums)

    inums = [int(n) for n in nums]

    for i in range(len(inums)):
        for j in range(i+1, len(inums)):
            if inums[i] > inums[j]:
                tmp = inums[i]
                inums[i] = inums[j]
                inums[j] = tmp

    print(inums[0])

