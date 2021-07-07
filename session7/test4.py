if __name__ == '__main__':
    n = int(input())

    nums = [int(n) for n in input().split(" ")]

    for i in range(n):
        for j in range(i, 0, -1):
            print("i: ", j-1)
            print("j: ", j)
            print(nums)
            print("nums[j]: ", nums[j-1])
            print("nums[i]: ", nums[i])

            if nums[j-1] < nums[j]:
                break

            tmp = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = tmp


    print(nums)
