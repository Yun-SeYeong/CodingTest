if __name__ == '__main__':
    N, K = input().split(" ")
    N = int(N)
    K = int(K)

    q = []

    for i in range(1, N + 1):
        q.append(i)

    print(q)

    current_count = 0
    while len(q) > 1:
        print(q)
        lo = (current_count + K - 1) % len(q)
        del q[lo]
        current_count = lo

    print(q[0])