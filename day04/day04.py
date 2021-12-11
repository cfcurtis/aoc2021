MARK_NUM = -1

def read_input(filename):
    with open(filename,'r') as f:
        called = [int(n) for n in f.readline().split(',')]
        boards = []
        board = []
        line = f.readline()
        while line != '':
            line = f.readline()
            if line.isspace() or line == '':
                if board is not None:
                    boards.append(board)
                board = []
            else:
                board.append([int(n) for n in line.split()])
    
    return called, boards

def print_board(board):
    for row in board:
        print("\t".join([str(r) for r in row]))

def calc_final_sum(board):
    final_sum = 0
    for row in board:
        for item in row:
            if item != MARK_NUM:
                final_sum += item
    
    return final_sum
    
def part_1(called,boards):
    winner = None  
    last_call = None
    for c in called:
        for b in range(len(boards)):
            board = boards[b]
            
            if winner is None:
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == c:
                            board[i][j] = MARK_NUM
                    # row
                    if sum(board[i]) == MARK_NUM * 5:
                        winner = b
                        last_call = c
                        break
                    
                # column
                if MARK_NUM * 5 in [sum(x) for x in zip(*board)]:
                    winner = b
                    last_call = c
                    break

    return calc_final_sum(boards[winner] * last_call)

def part_2(called,boards):
    winners = []
    last_win = []
    for c in called:
        for b in range(len(boards)):
            if b not in winners:
                board = boards[b]
                
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == c:
                            board[i][j] = MARK_NUM
                    # row
                    if sum(board[i]) == MARK_NUM * 5:
                        winners.append(b)
                        last_win.append(c)
                    
                # column
                if MARK_NUM * 5 in [sum(x) for x in zip(*board)]:
                    winners.append(b)
                    last_win.append(c)

    last = winners[-1]

    return calc_final_sum(boards[last] * last_win[-1])

if __name__ == '__main__':
    called, boards = read_input("input.txt")
    print(part_1(called, boards))
    print(part_2(called, boards))