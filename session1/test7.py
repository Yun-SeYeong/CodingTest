if __name__ == '__main__':
    num = int(input())
    nums = input().split(" ")

    print(num)
    print(nums)

    inums = [int(n) for n in nums]

    print(inums)

    result = 0
    for inum in inums:
        if inum % 10 == num % 10:
            result += 1

    print(result)