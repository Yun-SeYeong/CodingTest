if __name__ == '__main__':
    S = input()
    T = input()

    result = []
    for i in range(len(S)):
        print(S[i:i+len(T)])
        d = S[i:i+len(T)]

        is_equal = True

        m = {}
        m2 = {}

        for c in d:
            if m.get(c):
                m[c] += 1
            else:
                m[c] = 1

        for c in T:
            if m2.get(c):
                m2[c] += 1
            else:
                m2[c] = 1

        print(m)
        print(m2)

        for k in m if len(m) > len(m2) else m2:
            if m.get(k) != m2.get(k):
                is_equal = False

        if is_equal:
            result.append(d)

    print(len(result))