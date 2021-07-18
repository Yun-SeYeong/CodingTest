def get_num(m, c):
    print(c)
    result = []

    for c_pos in c:
        m[c_pos[0]+1][c_pos[1]] = 2
        if m[c_pos[0]+1][c_pos[1]] == 1:
            result.append([c_pos[0]+1, c_pos[1]])

        if m[c_pos[0]-1][c_pos[1]] == 1:
            result.append([c_pos[0]-1, c_pos[1]])

        if m[c_pos[0]][c_pos[1]+1] == 1:
            result.append([c_pos[0], c_pos[1]+1])

        if m[c_pos[0]][c_pos[1]-1] == 1:
            result.append([c_pos[0], c_pos[1]-1])

        if m[c_pos[0]+1][c_pos[1]+1] == 1:
            result.append([c_pos[0]+1, c_pos[1]+1])

        if m[c_pos[0]-1][c_pos[1]-1] == 1:
            result.append([c_pos[0]-1, c_pos[1]-1])

        if m[c_pos[0]+1][c_pos[1]-1] == 1:
            result.append([c_pos[0]+1, c_pos[1]-1])

        if m[c_pos[0]-1][c_pos[1]+1] == 1:
            result.append([c_pos[0]-1, c_pos[1]+1])

    get_num(m, result)

    return m


if __name__ == '__main__':
    m = []

    n = int(input())
    for _ in range(n):
        m.append([int(i) for i in input().split(" ")])

    print(m)

    result = 2

    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                m = get_num(m, [[i, j]])

    print(m)