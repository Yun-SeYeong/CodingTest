if __name__ == '__main__':
    first = input().split(" ")
    N = int(first[0])
    M = int(first[1])

    prices = []
    for i in range(N):
        prices.append([int(n) for n in input().split()])

    print(prices)

    prices.sort(key=lambda x: x[0]+x[1])

    print(prices)

    total_price = M
    result = 0
    for price in prices:
        print(total_price)
        print(price)
        if total_price - (price[0] + price[1]) < 0:
            break
        else:
            total_price -= (price[0] + price[1])
            result += 1

    if total_price - ((price[0] + price[1])/2) >= 0:
        total_price -= int((price[0] + price[1])/2)
        result += 1
        print(total_price)
        print(price)

    print(result)
