if __name__ == '__main__':
    N = int(input())
    strings = []
    for _ in range(N):
        strings.append(input())

    result = ""
    for s in strings:
        if len(result) < len(s):
            result = s

    print(result)