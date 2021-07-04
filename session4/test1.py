if __name__ == "__main__":
    N = int(input())

    nums = input().split(" ")
    inums = [int(n) for n in nums]

    result = []

    for i, inum in enumerate(inums):
        total = 0
        dig = 0
        while inum > 0:
            total += inum % 10
            inum = int(inum / 10)
            dig += 1

        result.append([inums[i], total])
        dig = 0

    result.sort(key=lambda x: (-x[1], -x[0]))

    print(result[0][0])
