if __name__ == '__main__':
    s = input()

    stack = []
    result = ""
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            while stack[-1] != "(":
                del stack[-1]
            del stack[-1]
        elif len(stack) == 0:
            result += c
        else:
            stack.append(c)

    print(result)