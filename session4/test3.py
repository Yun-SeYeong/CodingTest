if __name__ == '__main__':
    N, M = input().split(" ")
    N = int(N)
    M = int(M)

    tests = []
    for i in range(M):
        tests.append([int(n) for n in input().split(" ")])

    index_tests = []

    for test in tests:
        line = []
        for j, student in enumerate(test):
            line.append([student, j])
        line.sort(key=lambda x: x[0])
        index_tests.append(line)

    result = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                is_matched = True
                for test in index_tests:
                    if test[i][1] < test[j][1]:
                        is_matched = False
                if is_matched:
                    result += 1

    print(result)