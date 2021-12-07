def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle14/input.txt", "r")
    f = f.readlines()
    f = "".join(f).split(",")
    f = [int(x) for x in f]
    dicio = {10:0}
    for i in range(9):
        dicio[i]=0

    for i in f:
        if(i in dicio):
            dicio[i] +=1
        else:
            dicio[i] = 1
    cycles = 256
    keys = list(dicio.keys())
    for i in range(cycles):
        for item in dicio:
            if(item ==10 or item==8):
                continue
            if item ==0:
                dicio[8]+= dicio[0]
                dicio[6]+= dicio[0]
                dicio[10] += dicio[0]
                dicio[0] = 0
            if(item+1 ==6 or item+1==8):
                dicio[item] += (dicio[item+1]-dicio[10])
                dicio[item+1] = dicio[10]
                continue
            dicio[item]  += dicio[item+1] 
            dicio[item+1] = 0
        dicio[10]=0

    soma = 0
    for i in dicio:
        soma += dicio[i]
    print(soma)

solution()