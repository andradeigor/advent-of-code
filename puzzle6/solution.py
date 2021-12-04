def findshit(f,bit,switch):
    lista = [0,0]
    lista0 = []
    lista1 = []
    for item in f:
        if(item[bit]=='1'):
            lista1.append(item)
            lista[1] +=1 
        else:
            lista0.append(item)
            lista[0] +=1
    if(switch):
        if(lista[1] >=lista[0]):
            return lista1
        else:
            return lista0
    else:
        if(lista[0]<=lista[1]):
            return lista0
        else:
            return lista1

def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle5/input.txt", "r")
    f = f.readlines()
    f = [x.strip() for x in f]
    f2 = f[::]
    bit1 = 0
    bit2 = 0
    while(1):
        if(len(f)!=1):
            f = findshit(f,bit1,True)
            bit1+=1
        if(len(f2)!=1):
            f2 = findshit(f2,bit2,False)
            bit2+=1
        if(len(f)==1 and len(f2) ==1):
            break
    print(int(f[0],2)*int(f2[0],2))
    



solution()