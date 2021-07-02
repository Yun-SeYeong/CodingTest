
if __name__ == '__main__':
    nums = input().split(" ")

    inums = [int(n) for n in nums]

    for i in range(len(inums)):
        for j in range(i+1, len(inums)):
            if inums[i] < inums[j]:
                tmp = inums[j]
                inums[j] = inums[i]
                inums[i] = tmp

    print(inums[-1])
