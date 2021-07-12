def get_num(num_list, n):
    if n < 2:
        return [[n] for n in num_list]

    result = []
    for num2 in get_num(num_list, n - 1):
        for num1 in num_list:
            t = num2.copy()
            t.append(num1)
            result.append(t)

    return result


if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]

    nums = [i+1 for i in range(first[0])]

    result = get_num(nums, first[1])
    for r in result:
        print(" ".join([str(s) for s in r]))
