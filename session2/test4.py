if __name__ == '__main__':
    N = int(input())
    nums = input().split(" ")

    inums = [int(n) for n in nums]

    combo = 0
    result = 0
    for inum in inums:
        if inum == 0:
            combo = 0
        else:
            combo += inum

        print(combo)
        result += combo

    print(result)