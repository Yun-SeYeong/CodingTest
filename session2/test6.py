if __name__ == '__main__':
    N = int(input())

    nums = []
    for _ in range(N):
        row = [int(n) for n in input().split()]
        nums.append(row)

    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0


    for i in range(N):
        if sum(nums[i]) > result1:
            result1 = sum(nums[i])

        v_sum = 0
        for j in range(N):
            if i == j:
                result3 += nums[i][j]

            if i + j == N - 1:
                result4 += nums[i][j]
            v_sum += nums[j][i]

        if v_sum > result2:
            result2 = v_sum

    print(max(result1, result2, result3, result4))