if __name__ == '__main__':
    s = input().lower()
    reverse_s = s[::-1]

    l = len(s)

    half_l = int(l / 2)

    if s[:half_l] == reverse_s[:half_l]:
        print("YES")