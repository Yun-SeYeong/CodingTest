if __name__ == '__main__':
    s = input()

    pre = ""
    result = ""
    for c in s:
        if c in pre:
            continue

        pre += c
        result += c

    print(result)