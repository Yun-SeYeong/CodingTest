if __name__ == '__main__':
    N = int(input())

    meetings = []
    for _ in range(N):
        meetings.append([int(n) for n in input().split(" ")])

    result = 0
    for i in range(N):
        room = [meetings[i]]
        for j in range(i+1, N):
            print("=====")
            is_able = True
            for r in room:
                if r[0] < meetings[j][0] < r[1] or r[0] < meetings[j][1] < r[1]:
                    is_able = False
            if is_able:
                room.append(meetings[j])
        if result < len(room):
            result = len(room)

        print(room)

    print(result)