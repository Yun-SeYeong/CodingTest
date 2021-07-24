def get_num(nums, i):
    print(i)
    print(nums)

    result = []
    for num in nums:
        for i in range(len(num[0])):
            t1 = num[0].copy()
            t2 = num[1].copy()

            if len(t2) <= 0 or t1[i] > max(t2):
                t2.append(t1[i])
                del t1[:i]
                result.append([t1, t2])
    print(result)
    if len(result) <= 0:
        print(result)
        return

    get_num(result, i+1)



if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split(" ")]

    get_num([[nums, []]], 0)