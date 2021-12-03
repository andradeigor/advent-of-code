def comonbit(f,lista,bit):
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
    if(lista[1]>=lista[0]):

        return lista1
    else:

        return lista0
def lesbit(f,bit):
    lista = [0,0]
    lista0 = []
    lista1 = []
    for item in f:
        if(item[bit]=='1'):
            lista1.append(item)
            lista[1] +=1 
        elif(item[bit]=='0'):
            lista0.append(item)
            lista[0] +=1
    if(lista[0]<=lista[1]):
        return lista0
    else:
        return lista1
def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle5/input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n", "") for x in f]
    f2 = f[::]
    listaDeNumeros = []
    listaDeNumeros2 = []
    for i in range(12):
        listaDeNumeros.append([0,0])
        listaDeNumeros2.append([0,0])
    bit = 0
    while(1):
        f = comonbit(f,listaDeNumeros,bit)
        bit+=1
        if(len(f)==1):
            break
    bit = 0
    while(1):
        f2 = lesbit(f2,bit)
        bit+=1
        if(len(f2)==1):
            break
    print(f,f2)
    



solution()