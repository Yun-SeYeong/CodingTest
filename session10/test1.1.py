
num = int(input())


def dfs(n):
    print(n)
    if n + 1 > num or n + 2 > num:
        return 1

    return dfs(n+1) + dfs(n+2)


print(dfs(0))



