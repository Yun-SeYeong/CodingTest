if __name__ == '__main__':
    n = int(input())
    nums = [int(i) for i in input().split(" ")]

    m = int(input())

    result = 0

    while m > 0:
        print(m)
        if m / nums[-1] >= 1:
            m -= nums[-1]
            result += 1
        else:
            del nums[-1]

    print(result)