if __name__ == '__main__':
    s = input()

    result = ""
    for c in s:
        if ord("0") <= ord(c) <= ord("9"):
            result += c

    print(int(result))
