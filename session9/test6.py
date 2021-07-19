def get_num(m, c):
    if len(c) <= 0:
        return m
    result = []

    for c_pos in c:
        if m[c_pos[0]][c_pos[1]] == 1:
            m[c_pos[0]][c_pos[1]] = 2

        if c_pos[0] < len(m)-1 and m[c_pos[0]+1][c_pos[1]] == 1:
            result.append([c_pos[0]+1, c_pos[1]])

        if c_pos[0] > 0 and m[c_pos[0]-1][c_pos[1]] == 1:
            result.append([c_pos[0]-1, c_pos[1]])

        if c_pos[1] < len(m)-1 and m[c_pos[0]][c_pos[1]+1] == 1:
            result.append([c_pos[0], c_pos[1]+1])

        if c_pos[1] > 0 and m[c_pos[0]][c_pos[1]-1] == 1:
            result.append([c_pos[0], c_pos[1]-1])

        if c_pos[0] < len(m)-1 and c_pos[1] < len(m)-1 and m[c_pos[0]+1][c_pos[1]+1] == 1:
            result.append([c_pos[0]+1, c_pos[1]+1])

        if c_pos[0] > 0 and c_pos[1] > 0 and m[c_pos[0]-1][c_pos[1]-1] == 1:
            result.append([c_pos[0]-1, c_pos[1]-1])

        if c_pos[0] < len(m)-1 and c_pos[1] > 0 and m[c_pos[0]+1][c_pos[1]-1] == 1:
            result.append([c_pos[0]+1, c_pos[1]-1])

        if c_pos[0] > 0 and c_pos[1] < len(m)-1 and m[c_pos[0]-1][c_pos[1]+1] == 1:
            result.append([c_pos[0]-1, c_pos[1]+1])
    m = get_num(m, result)

    return m


if __name__ == '__main__':
    m = []

    n = int(input())
    for _ in range(n):
        m.append([int(i) for i in input().split(" ")])

    print(m)

    result = 0

    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                m = get_num(m, [[i, j]])
                result += 1

    print(result)
