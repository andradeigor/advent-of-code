def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle10/input.txt", "r")
    f = f.readlines()
    f = [x.replace(" ", "").replace("\n","").replace("->",",").split(",") for x in f]
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    board = []
    maxx2= 0
    maxy2= 0
    maior = 0
    for i in f:
        x1.append(int(i[0]))
        if(int(i[0])>maxx2):
            maxx2=int(i[0])
        if(int(i[1])>maxy2):
            maxy2=int(i[1])
        y1.append(int(i[1]))
        if(int(i[2])>maxx2):
            maxx2=int(i[2])
        x2.append(int(i[2]))
        y2.append(int(i[3]))
        if(int(i[3])>maxy2):
            maxy2=int(i[3])        
    if(maxx2>maxy2):
        maior = maxx2
    else:
        maior = maxy2
    for i in range(maior+1):
        temp = []
        for j in range(maior+1):
            temp.append(".")
        board.append(temp)
    soma=[]

    for i in range(len(x1)):
        if(x1[i]==x2[i]):
            if(y1[i]<y2[i]):
                for j in range(y1[i],y2[i]+1):
                    if(board[j][x1[i]] !="."):
                        board[j][x1[i]]+=1
                        if( [[j],[x1[i]]] not in soma):
                            soma.append([[j],[x1[i]]])
                    else:
                        board[j][x1[i]] = 1
            elif(y1[i]>y2[i]):
                for j in range(y2[i],y1[i]+1):
                    if(board[j][x1[i]] !="."):
                        board[j][x1[i]]+=1
                        if( [[j],[x1[i]]] not in soma):
                            soma.append([[j],[x1[i]]])
                    else:
                        board[j][x1[i]] = 1
        elif(y1[i]==y2[i]):
            if(x1[i]<x2[i]):
                for k in range(x1[i],x2[i]+1):
                    if(board[y1[i]][k] !="."):
                        board[y1[i]][k]+=1
                        if([[y1[i]],[k]] not in soma):
                            soma.append([[y1[i]],[k]])
                    else:
                        board[y1[i]][k]=1
            elif(x1[i]>x2[i]):
                for k in range(x2[i],x1[i]+1):
                    if(board[y1[i]][k] !="."):
                        board[y1[i]][k]+=1
                        if( [[y1[i]],[k]] not in soma):
                            soma.append([[y1[i]],[k]])
                    else:
                        board[y1[i]][k]=1
        else:
            if(x1[i]!=x2[i] and y1[i]!=y2[i]):
                delta = abs(x2[i]-x1[i])
                newx = x1[i]
                newy = y1[i]
                for k in range((delta)+1):
                    newx = x1[i]-k if x2[i]<x1[i] else x1[i]+k
                    newy = y1[i]-k if y2[i]<y1[i] else y1[i]+k
                    if(board[newy][newx]!="."):
                        board[newy][newx] +=1
                        if([[newy],[newx]] not in soma):
                            soma.append([[newy],[newx]])
                    else:
                        board[newy][newx] = 1
                    
            elif(x1[i]<x2[i]):
                for k in range(x1[i],x2[i]+1):
                    if(board[k][k] !="."):
                        board[k][k]+=1
                        if([[k],[k]] not in soma):
                            soma.append([[k],[k]])
                    else:
                        board[k][k]=1
            elif(x2[i]<x1[i]):
                for k in range(x2[i],x1[i]+1):
                    if(board[k][k] !="."):
                        board[k][k]+=1
                        if([[k],[k]] not in soma):
                            soma.append([[k],[k]])
                    else:
                        board[k][k]=1

    print(len(soma))



solution()