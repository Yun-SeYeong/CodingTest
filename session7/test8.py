if __name__ == '__main__':
    N = int(input())

    meetings = []
    for _ in range(N):
        meetings.append([int(n) for n in input().split(" ")])


    for i in range(N):
        room = [meetings[i]]
        for j in range(i+1, N):
            for r in room:
                if r[1] <= meetings[j][0] or r[0] >= meetings[j][1]:
                    room.append(r)

        print(room)



