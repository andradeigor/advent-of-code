def forward(levels,move):
    levels = [levels[0]+move,levels[1]+(levels[2]*move),levels[2]]
    return levels
def up(levels,move):
    levels = [levels[0],levels[1], levels[2]-move]
    return levels
def down(levels,move):
    levels = [levels[0],levels[1], levels[2]+move]
    return levels

def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle5/input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n", "") for x in f]
    dicionario = {}
    for i in range(12):
        dicionario[i] = [0,0]
    for number in f:
        for bit in range(len(number)):
            if(int(number[bit])==1):
                dicionario[int(bit)][1] +=1 
            else:
                dicionario[int(bit)][0] +=1
    gamma = ""
    for item in dicionario:
        if(dicionario[item][0]>dicionario[item][1]):
            gamma+="0"
        else:
            gamma+="1"
    print(gamma)



solution()