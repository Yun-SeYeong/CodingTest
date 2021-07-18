def get_num(c, t, deep):
    print(c)
    result = []
    for n in c:
        if n < 0 or n >= 10000:
            return

        if n + 1 == t:
            print("n: ", deep + 1)
            return

        if n + -1 == t:
            print("n: ", deep + 1)
            return

        if n + 5 == t:
            print("n: ", deep + 1)
            return

        result.append(n + 1)
        result.append(n - 1)
        result.append(n + 5)

    get_num(result, t, deep + 1)


if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]

    print(get_num([first[0]], first[1], 1))