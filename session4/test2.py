if __name__== '__main__':

    N = int(input())

    nums = input().split(" ")
    inums = [int(n[::-1]) for n in nums]
    print(inums)

    result = []

    for i, inum in enumerate(inums):
        prime_num = True
        for j in range(2, inum):
            if inum % j == 0:
                prime_num = False
                break
        if prime_num and inum != 1:
            result.append(inum)

    print(result)
