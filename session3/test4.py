if __name__ == "__main__":
    input_string = input().split(" ")

    s = input_string[1]
    t = input_string[0]

    result = []

    for i, ic in enumerate(t):
        if ic == s:
            for j, _ in enumerate(t):
                if len(result) >= len(t):
                    if result[j] > abs(i - j):
                        result[j] = abs(i - j)
                else:
                    result.append(abs(i - j))

    print(" ".join([str(x) for x in result]))
