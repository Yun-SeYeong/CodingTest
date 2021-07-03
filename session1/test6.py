if __name__ == '__main__':
    nums = input().split(" ")
    print(nums)

    inums = [int(n) for n in nums]

    result1 = 0
    result2 = None

    for inum in inums:
        if inum % 2 == 1:
            if result2:
                if inum < result2:
                    result2 = inum
            else:
                result2 = inum
            result1 += inum

    print(result1)
    print(result2)
