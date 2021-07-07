if __name__ == '__main__':
    s1 = input()
    s2 = input()

    count = 0
    q = []
    for c in s2:
        print(c)
        print(s1[count: count+1])
        print("=====")
        if s1[count: count+1] == c:
            q.append(c)
            count += 1

    print("".join(q))
    print("YES" if "".join(q) == s1 else "NO")