if __name__ == '__main__':
    nums = input().split(" ")
    print(nums)

    inums = [int(n) for n in nums]

    print(inums)

    if inums[0] < inums[1] + inums[2] and inums[1] < inums[0] + inums[2] and inums[2] < inums[0] + inums[1]:
        print("YES")
    else:
        print("NO")

