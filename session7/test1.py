if __name__ == '__main__':
    n = int(input())

    nums = [int(n) for n in input().split(" ")]

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            print("nums[min_index] :", nums[min_index])
            print("nums[j] :", nums[j])
            if nums[min_index] > nums[j]:
                min_index = j

        print("i: ", i)
        print("min_index: ", min_index)

        tmp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = tmp

    print(nums)