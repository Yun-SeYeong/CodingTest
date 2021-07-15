def get_num(m, x, y, bx, by, h):
    print(x, " ", y, " ", bx, " ", by, " ", h)

    if x == 6 and y == 6:
        print("success")
        return 1

    # if bx == 0 and by == 0:
    #     return 0

    result = 0
    if x > 0 and m[x-1][y] == 0 and [x-1, y] not in h:
        print("m[x-1][y]: ", m[x-1][y])
        t = h.copy()
        t.append([x-1, y])
        result += get_num(m, x-1, y, x, y, t)

    if x < 6 and m[x+1][y] == 0 and [x+1, y] not in h:
        print("m[x+1][y]: ", m[x+1][y])
        t = h.copy()
        t.append([x+1, y])
        result += get_num(m, x+1, y, x, y, t)

    if y > 0 and m[x][y-1] == 0 and [x, y-1] not in h:
        print("m[x][y-1]: ", m[x][y-1])
        t = h.copy()
        t.append([x, y-1])
        result += get_num(m, x, y-1, x, y, t)

    if y < 6 and m[x][y+1] == 0 and [x, y+1] not in h:
        print("m[x][y+1]: ", m[x][y+1])
        t = h.copy()
        t.append([x, y+1])
        result += get_num(m, x, y+1, x, y, t)

    return result


if __name__ == '__main__':
    m = []
    for i in range(7):
        m.append([int(n) for n in input().split(" ")])

    print(get_num(m, 0, 0, -1, -1, [[0, 0]]))
