if __name__ == '__main__':
    s = input()

    stack = []
    for c in s:
        print(c)
        if len(stack) >= 2 and c == "+":
            r = int(stack[-2]) + int(stack[-1])
            del stack[-1]
            del stack[-1]
            stack.append(r)
        elif len(stack) >= 2 and c == "-":
            r = int(stack[-2]) - int(stack[-1])
            del stack[-1]
            del stack[-1]
            stack.append(r)
        elif len(stack) >= 2 and c == "*":
            r = int(stack[-2]) * int(stack[-1])
            del stack[-1]
            del stack[-1]
            stack.append(r)
        elif len(stack) >= 2 and c == "/":
            r = int(stack[-2]) / int(stack[-1])
            del stack[-1]
            del stack[-1]
            stack.append(r)
        else:
            stack.append(c)
        print(stack)

    print(stack[0])
