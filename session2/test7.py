if __name__ == '__main__':
    N = int(input())

    nums = []

    for _ in range(N):
        nums.append([int(n) for n in input().split(" ")])

    print(nums)

    result = 0
    for i in range(N):
        for j in range(N):
            if nums[i][j] == max(nums[i][j],
                                 nums[i-1][j] if i-1 >= 0 else 0,
                                 nums[i+1][j] if i+1 < N else 0,
                                 nums[i][j-1] if j-1 >= 0 else 0,
                                 nums[i][j+1] if j+1 < N else 0):
                print("======")
                print(nums[i][j])
                result += 1

    print(result)