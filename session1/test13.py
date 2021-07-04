if __name__ == '__main__':
    str = input()

    result = ""
    for s in str:
        if 65 <= ord(s) <= 90:
            result += s.lower()
        else:
            result += s.upper()

    print(result)
