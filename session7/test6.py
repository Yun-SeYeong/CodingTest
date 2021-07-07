if __name__ == '__main__':
    N = int(input())

    nums = [int(n) for n in input().split(" ")]

    sorted_nums = sorted(nums)

    result = []
    for i in range(N):
        if nums[i] != sorted_nums[i]:
            result.append(str(i+1))

    print(" ".join(result))