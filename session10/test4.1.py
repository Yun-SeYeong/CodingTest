
count = 3
units = [int(i) for i in "10 500 1000".split(" ")]
num = 1520


def bfs(n):
    result = 0
    queue = n[:]

    while queue:
        result += 1
        next_queue = []
        for q in queue:
            print("q: ", q)

            for u in units:
                if q - u > 0:
                    next_queue.append(q - u)
                elif q - u == 0:
                    return result
        print("next_queue: ", next_queue)

        queue = next_queue[:]
    return result


print(bfs([num]))
