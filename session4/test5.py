if __name__ == '__main__':
    first = input().split(" ")
    N = int(first[0])
    K = int(first[1])

    nums = input().split(" ")

    inums = [int(n) for n in nums]

    inums.sort(reverse=True)

    print(inums)

    top_nums = []

    for inum in inums:
        if len(top_nums) < K and inum not in top_nums:
            top_nums.append(inum)

    print(sum(top_nums))