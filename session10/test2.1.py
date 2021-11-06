num = int(input())


def dfs(n):
    if n >= num:
        return 1

    return dfs(n + 1) + dfs(n + 2)


print(dfs(0))
