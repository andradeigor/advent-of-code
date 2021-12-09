from collections import deque
def possibleMoves(board, target):
    up = [target[0]-1,target[1]]  if target[0]-1 >= 0 else None
    left = [target[0],target[1]-1] if target[1]-1 >= 0 else None
    down = [target[0]+1 ,target[1]] if target[0]+1 < len(board) else None
    right = [target[0],target[1]+1] if target[1]+1 <len(board[0]) else None
    return [up,down,right,left]

def possibleBassin(board,target):
    up = [target[0]-1,target[1]]  if target[0]-1 >= 0 and (board[target[0]][target[1]]+1 <= board[target[0]-1][target[1]]) and( board[target[0]-1][target[1]] !=9) else None
    left = [target[0],target[1]-1] if target[1]-1 >= 0 and (board[target[0]][target[1]]+1 <= board[target[0]][target[1]-1]) and board[target[0]][target[1]-1]!=9 else None
    down = [target[0]+1 ,target[1]] if target[0]+1 < len(board) and (board[target[0]][target[1]]+1 <= board[target[0]+1][target[1]]) and board[target[0]+1][target[1]]!=9 else None
    right = [target[0],target[1]+1] if target[1]+1 <len(board[0]) and (board[target[0]][target[1]]+1 <= board[target[0]][target[1]+1]) and board[target[0]][target[1]+1]!=9 else None
    return [up,down,right,left]

def bassinSum(board,lista):
    soma = 0
    for item in lista:
        soma+= (board[item[0]][item[1]] +1)
    return soma


def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle18/input.txt", "r")
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
                lower.append([target[0],target[1]])

    basin = {}
    totalSum = []
    for low in lower:
        queue = deque([low])
        currentTarget = low
        while(queue):
            mytarget = queue.popleft()
            ba = possibleBassin(board,mytarget)
            for i in ba:
                if(i):
                    queue.append(i)
                    if(str(currentTarget) not in basin):
                        basin[str(currentTarget)] = [currentTarget, i] 
                    else:
                        if(i not in basin[str(currentTarget)]):
                            basin[str(currentTarget)].append(i)
        if(str(currentTarget) not in basin):
            continue 
        currentSum = len(basin[str(currentTarget)])
        if(len(totalSum)<3):
            totalSum.append(currentSum)
        else:
            minimo = min(totalSum)
            if(currentSum > minimo):
                totalSum.remove(minimo)
                totalSum.append(currentSum)
    soma = 1
    for i in totalSum:
        soma *= i
    print(soma)



    

solution()