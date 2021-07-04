if __name__ == '__main__':
    str = input()
    search_str = input()

    count = 0
    for s in str:
        if s == search_str:
            count += 1

    print(count)
