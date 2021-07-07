if __name__ == '__main__':
    N = int(input())
    n_nums = [int(n) for n in input().split(" ")]
    M = int(input())
    m_nums = [int(m) for m in input().split(" ")]

    long_nums = sorted(n_nums if N >= M else m_nums)
    short_nums = n_nums if N < M else m_nums

    result = []
    for i in range(len(long_nums)):
        if long_nums[i] in short_nums:
            result.append(long_nums[i])


    print(result)
