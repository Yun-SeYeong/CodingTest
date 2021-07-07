if __name__ == '__main__':
    s = input()

    stack_count = 0
    stack = []

    stick_count = 0

    for c in s:
        if len(stack) > 0 and stack[-1] == "(" and c == ")":
            stick_count += stack_count
            print(stack)
            print(stack_count)
        elif len(stack) > 0 and stack[-1] == "(" and c == "(":
            stack_count += 1
        elif len(stack) > 0 and stack[-1] == ")" and c == ")":
            stack_count -= 1
            stick_count += 1

        stack.append(c)

    print(stick_count)