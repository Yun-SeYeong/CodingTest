def get_num(nums, target):
    if target <= 0:
        return 0

    print(target)

    for num in nums:
        return get_num(nums, target-num)+1


if __name__ == '__main__':
    N = int(input())
    nums = [int(n) for n in input().split(" ")]
    M = int(input())

    print(get_num(sorted(nums, reverse=True), M))
