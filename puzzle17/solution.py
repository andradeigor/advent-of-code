def possibleMoves(board, target):
    up = [target[0]-1,target[1]]  if target[0]-1 >= 0 else None
    left = [target[0],target[1]-1] if target[1]-1 >= 0 else None
    down = [target[0]+1 ,target[1]] if target[0]+1 < len(board) else None
    right = [target[0],target[1]+1] if target[1]+1 <len(board[0]) else None
    return [up,down,right,left]


def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle17/input.txt", "r")
    f = f.readlines()
    board = [list(x.replace("\n","").strip()) for x in f]
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = int(board[i][j])
    lower = []
    for line in range(len(board)):
        for row in range(len(board[line])):
            target = [line,row]
            possible = possibleMoves(board,target)
            canAdd = True
            for move in possible:
                if(move and board[target[0]][target[1]] >= board[move[0]][move[1]]):
                    canAdd = False
            if(canAdd):
                lower.append(board[target[0]][target[1]])
    soma = 0
    for i in lower:
        soma += (i+1) 
    
    print(soma)


    

solution()