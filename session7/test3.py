if __name__ == '__main__':
    n = int(input())

    nums = [int(n) for n in input().split(" ")]

    for i in range(n):
        for j in range(1, n-i):
            print("j: ", j)
            if nums[j-1] > 0 and nums[j] < 0:
                tmp = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = tmp
            print(nums)

    print(nums)