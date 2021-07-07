if __name__ == '__main__':
    a = input()
    b = input()

    is_equal = True
    for c in b:
        if c not in b:
            is_equal = False


    print("YES" if is_equal else "NO")