if __name__ == '__main__':
    str = input()

    count = 0
    for s in str:
        if 65 <= ord(s) <= 90:
            count += 1

    print(count)
