if __name__ == '__main__':
    num = int(input())

    s = input()

    t = {}
    for c in s:
        if t.get(c):
            t[c] += 1
        else:
            t[c] = 1

    print(sorted(t.items(), key=lambda x: -x[1])[0][0])