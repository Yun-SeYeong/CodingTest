if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]
    nums = []
    for i in range(first[0]):
        nums.append([int(x) for x in input().split(" ")])

    result = first[1]

    nums = sorted(nums, key= lambda x: x[0]/x[1])

    print(nums)

    score = 0
    while True:
        result -= nums[-1][1]
        if result < 0:
            break
        score += nums[-1][0]
        del nums[-1]

    print(score)