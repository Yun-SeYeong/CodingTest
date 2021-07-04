if __name__ == '__main__':
    N = int(input())

    nums = input().split(" ")

    inums = [int(n) for n in nums]

    result = []

    for i, inum in enumerate(inums):
        result.append([i+1, inum])

    print(sorted(result, key=lambda x: (-x[1], x[0])))
