def get_num(m, points, c, h):
    result = 0

    for i in m.get(c):
        if i not in h:
            if i == points:
                result += 1
            else:
                t = h.copy()
                t.append(i)
                result += get_num(m, points, i, t)
    return result


if __name__== '__main__':
    map = {}

    first = [int(n) for n in input().split(" ")]

    for i in range(first[0]):
        map[i+1] = []

    for i in range(first[1]):
        m = [int(n) for n in input().split(" ")]
        map[m[0]].append(m[1])

    print(map)

    result = 0
    print(get_num(map, first[0], 1, [1]))