count = 8
nums = [int(i) for i in "5 3 7 8 6 2 9 4".split(" ")]
print(nums)


dp = [1 for i in range(len(nums))]

print(dp)

for i in range(1, count):
    for j in range(0, i):
        print("i: ", i, "j: ", j)
        if nums[i] > nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            print("dp: ", dp)

print(max(dp))