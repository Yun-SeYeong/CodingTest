def get_num(nums, total, m, n):
    if len(total) >= n or len(nums) <= 0:
        return []

    result = []
    for i in range(len(nums)):

        for j in range(i, i+1):
            t1 = nums.copy()
            t2 = total.copy()
            t2.append(t1[j])
            del t1[j]

            # print("t1: ", t1)
            # print("t2: ", t2)

            if len(t2) < n or len(t1[j:]) > 0:
                r = get_num(t1[j:], t2, m, n)
                if len(r) > 1:
                    result.append(r)
                elif len(r) == 1:
                    for rn in r:
                        result.append(rn)

            else:
                if sum(t2) % m == 0:
                    return t2
                break
    return result



if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]
    second = [int(n) for n in input().split(" ")]
    m = int(input())

    print(len(get_num(second, [], m, first[1])))