if __name__ == '__main__':
    board = eval(input())
    moves = eval(input())

    print(board)
    print(moves)

    stack = []
    count = 0
    for move in moves:
        for i in range(len(board)):
            print("move:", move)
            print("i:", i)
            print("value:", board[i][move-1])
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move - 1] = 0
                break
        print(stack)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            del stack[-1]
            del stack[-1]
            count += 1

    print(count * 2)