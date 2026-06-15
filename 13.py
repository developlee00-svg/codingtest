def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        i-=1
        for j in range(5):
            if board[j][i] != 0 :
                if stack and stack[-1] == board[j][i]:
                    stack.pop()
                    board[j][i] = 0
                    answer+=2
                    break
                stack.append(board[j][i])
                board[j][i] = 0
                break
        
    return answer




board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]
moves = [1, 1, 2, 3, 2, 4]
print(solution(board, moves))