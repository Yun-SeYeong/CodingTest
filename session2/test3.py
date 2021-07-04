if __name__ == '__main__':
    N = int(input())
    num_a = input().split(" ")
    num_b = input().split(" ")

    for i in range(N):
        if ((int(num_a[i]) - 1 + 1) % 3) == int(num_b[i]) - 1:
            print("B")
        elif (int(num_a[i]) - 1) % 3 == int(num_b[i]) - 1:
            print("D")
        elif int(num_a[i]) - 1 == (int(num_b[i]) - 1 + 1) % 3:
            print("A")

