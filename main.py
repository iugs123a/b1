import random

# 打印棋盘
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

# 检查胜者
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_max, alpha, beta, computer, player):
    winner = check_winner(board)
    if winner == computer:
        return 10 - depth
    elif winner == player:
        return depth - 10
    elif is_draw(board):
        return 0

    if is_max:
        max_eval = float('-inf')
        for i, j in get_valid_moves(board):
            board[i][j] = computer
            score = minimax(board, depth + 1, False, alpha, beta, computer, player)
            board[i][j] = ' '
            max_eval = max(max_eval, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_valid_moves(board):
            board[i][j] = player
            score = minimax(board, depth + 1, True, alpha, beta, computer, player)
            board[i][j] = ' '
            min_eval = min(min_eval, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_eval

def computer_move(board, computer, player):
    best_score = float('-inf')
    best_move = None
    for i, j in get_valid_moves(board):
        board[i][j] = computer
        score = minimax(board, 0, False, float('-inf'), float('inf'), computer, player)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = computer

def player_move(board, player):
    while True:
        try:
            move = input("请输入你的落子坐标（行 列），范围为 0~2（如 1 1）: ")
            i, j = map(int, move.strip().split())
            if 0 <= i <= 2 and 0 <= j <= 2:
                if board[i][j] == ' ':
                    board[i][j] = player
                    break
                else:
                    print("该位置已有棋子，请重新输入。")
            else:
                print("请输入0~2之间的行列索引。")
        except Exception:
            print("输入格式错误，请输入两个数字，如 1 1")

def play_game():
    board = [[' ']*3 for _ in range(3)]
    first = random.choice(['player', 'computer'])
    player = random.choice(['X', 'O'])
    computer = 'O' if player == 'X' else 'X'

    print(f"你执棋 '{player}'，电脑执棋 '{computer}'")
    print(f"{'你先手！' if first == 'player' else '电脑先手！'}")
    print_board(board)

    turn = first
    while True:
        if turn == 'player':
            player_move(board, player)
            print_board(board)
            if check_winner(board) == player:
                print("你赢了！")
                break
            elif is_draw(board):
                print("平局！")
                break
            turn = 'computer'
        else:
            print("电脑思考中...")
            computer_move(board, computer, player)
            print_board(board)
            if check_winner(board) == computer:
                print("电脑赢了！")
                break
            elif is_draw(board):
                print("平局！")
                break
            turn = 'player'

if __name__ == "__main__":
    play_game()
