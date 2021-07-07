if __name__ == '__main__':
    n = int(input())

    nums = [int(n) for n in input().split(" ")]

    for i in range(n):
        for j in range(n-i-1):
            if nums[j+1] < nums[j]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp

    print(nums)