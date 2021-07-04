if __name__ == '__main__':
    N = int(input())

    strings = []
    for _ in range(N):
        strings.append(input())

    pre = []
    for string in strings:
        if string in pre:
            continue

        pre.append(string)

    for p in pre:
        print(p)