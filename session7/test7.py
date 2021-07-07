if __name__ == '__main__':
    N = int(input())

    points = []
    for i in range(N):
        points.append([int(n) for n in input().split()])

    for n in sorted(points, key=lambda x: (x[0], x[1])):
        print(str(n[0])+" "+str(n[1]))
