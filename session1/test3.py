if __name__ == '__main__':
    num = int(input())

    print(int(num/12) + (1 if num % 12 > 0 else 0))

