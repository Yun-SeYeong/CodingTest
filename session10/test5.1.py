#
# if __name__ == '__main__':
#     count, time = [int(i) for i in "4 5".split(" ")]
#
#     nums = [[3, 2], [4, 3], [5, 4], [6, 5]]
#
#     knapsack = [0 for i in range(time + 1)]
#
#     for i in range(count):
#         for j in range(time, 1, -1):
#             s = nums[i][0]
#             t = nums[i][1]
#
#             print("s: ", s)
#             print("t: ", t)
#
#             if j >= t:
#                 knapsack[j] = max(s + knapsack[j-t], knapsack[j])
#
#     print(knapsack)


count, time = [int(i) for i in "5 20".split(" ")]
nums = [[10, 5], [25, 12], [15, 8], [6, 3], [7, 4]]

knapsack = [0 for _ in range(time+1)]

print(knapsack)

for i in range(count):
    for j in range(time, 1, -1):
        s = nums[i][0]
        t = nums[i][1]

        if j >= t:
            knapsack[j] = max(knapsack[j], s + knapsack[j-t])

print(knapsack[-1])