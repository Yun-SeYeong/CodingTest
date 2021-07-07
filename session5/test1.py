if __name__ == '__main__':
    N = int(input())
    n_nums = [int(n) for n in input().split(" ")]
    M = int(input())
    m_nums = [int(m) for m in input().split(" ")]

    result = []

    for i in range(N if N > M else M):
        print("--------")
        print(i)
        if i >= len(n_nums):
            result.append(m_nums[i])
            print(m_nums[i])
            continue

        if i >= len(m_nums):
            result.append(n_nums[i])
            print(n_nums[i])
            continue

        print(n_nums[i])
        print(m_nums[i])

        if n_nums[i] < m_nums[i]:
            result.append(n_nums[i])
            result.append(m_nums[i])
        else:
            result.append(m_nums[i])
            result.append(n_nums[i])

    print(result)