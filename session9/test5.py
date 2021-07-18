def get_num(c, t, deep):
    result = []
    for n in c:
        if n < 0 or n >= 10000:
            return

        if n + 1 == t:
            return deep + 1

        if n + -1 == t:
            return deep + 1

        if n + 5 == t:
            return deep + 1

        result.append(n + 1)
        result.append(n - 1)
        result.append(n + 5)

    return get_num(result, t, deep + 1)


if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]

    print(get_num([first[0]], first[1], 0))