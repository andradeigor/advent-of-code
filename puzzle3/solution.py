def forward(levels,move):
    levels = [levels[0]+move,levels[1]]
    return levels
def up(levels,move):
    levels = [levels[0],levels[1]-move]
    return levels
def down(levels,move):
    levels = [levels[0],levels[1]+move]
    return levels

def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle3/input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n", "").split(" ") for x in f]
    moves = {'forward': forward,'up':up,'down':down }
    levels = [0,0]
    for item in f:
        levels = moves[item[0]](levels,int(item[1]))
    print(levels[0]*levels[1])


solution()