if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]
    second = [int(n) for n in input().split(" ")]

    b = [0 for _ in range(first[0])]
    for i in range(first[1]):
        for j in range(first[0]):
            print("j: ", j)
            if b[j] == second[i] or j == first[0]-1:
                print(j)
                for x in range(j, 0, -1):
                    tmp = b[x]
                    b[x] = b[x-1]
                    b[x-1] = tmp
                break

        b[0] = second[i]
        print(b)

    print(" ".join([str(n) for n in b]))