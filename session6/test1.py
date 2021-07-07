if __name__ == '__main__':
    s = input()

    stack = []

    for c in s:
        if c == "(":
            stack.append("(")
        else:
            if len(stack) > 0:
                del stack[-1]
            else:
                stack.append(c)
                break

    if len(stack) > 0:
        print("NO")
    else:
        print("YES")