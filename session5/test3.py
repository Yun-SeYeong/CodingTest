if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]

    second = [int(n) for n in input().split(" ")]

    count = 0
    print(first)
    result = []
    for i in range(first[0]):
        s = []
        for j in range(i, first[0]):
            s.append(second[j])
            total = sum(s)
            if total == first[1]:
                count += 1
                result.append(s)

            if total >= first[1]:
                break

    print(result)
    print(count)

