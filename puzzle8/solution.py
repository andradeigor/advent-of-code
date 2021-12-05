from collections import deque 

def confNumber(number,board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]==number):
                board[i][j] = 0
    return board
    
def confganhador(board):
    for linha in range(len(board)):
        if(sum(board[linha])==0):
            return [linha,0]
    for coluna in range(len(board)):
        ans = 0
        for linha in range(len(board[coluna])):
            ans += board[linha][coluna]
        if(ans ==0):
            return [0,coluna]
    return False
def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle8/input.txt", "r")
    f = f.readlines()
    f = deque([x.strip() for x in f])
    numbers = f.popleft().split(",")
    number = [int(x) for x in numbers]
    
    boards = []
    f = [value for value in f if value != ""]
    f = [x.split(" ") for x in f]
    for i in f:
        for j in i:
            if j=="":
                i.remove("")
    
    for i in range(len(f)):
        for j in range(len(f[i])):
            f[i][j] = int(f[i][j]) 
    j=0
    for i in range(len(f)+1):
        if(i!=0 and i%5==0):
            boards.append(f[j:i])
            j=i

    ganhador = []
    newboards = boards[::]
    indexganhadores = []
    for numero in numbers:
        if(len(ganhador) ==len(newboards)):
            break
        for index in range(len(newboards)):
            newboards[index]= confNumber(int(numero), newboards[index])
            ganhou = confganhador(newboards[index])
            if(ganhou !=False):
                if([index,numero] not in ganhador):
                    if(index not in indexganhadores):
                        indexganhadores.append(index)
                        ganhador.append([index,numero])
                        if(len(ganhador) ==len(newboards)):
                            break
    soma =0
    for i in newboards[ganhador[-1][0]]:
        for linha in i:
            soma+=linha
    print(soma*int(ganhador[-1][1]))




solution()