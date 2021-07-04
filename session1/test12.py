if __name__ == '__main__':
    str = input()

    result = ""
    print(ord("a"))
    print(ord("z"))
    for s in str:
        if 97 <= ord(s) <= 122:
            result += s.upper()

    print(result)

