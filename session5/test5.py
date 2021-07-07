if __name__ == '__main__':
    first = [int(n) for n in input().split(" ")]
    second = [int(n) for n in input().split()]

    result = 0
    for i in range(first[0]):
        if result < sum(second[i:i+3]):
            result = sum(second[i:i+3])

    print(result)

