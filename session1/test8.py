if __name__ == '__main__':
    nums = input().split(" ")

    print(nums)

    inums = [int(n) for n in nums]

    print(inums)

    total = sum(inums)

    for i in range(len(inums)):
        for j in range(i+1, len(inums)):
            if total - inums[i] - inums[j] == 100:
                print(inums[i])
                print(inums[j])
                del inums[i]
                del inums[j - 1]
                break

        if len(inums) == 7:
            break

    print(inums)
    print(sum(inums))
