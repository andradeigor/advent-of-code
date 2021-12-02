
def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle2/input.txt", "r")
    f = f.readlines()
    f = [int(x[:-1]) for x in f]
    gratest = 0
    prev = f[0] + f[1]+ f[2]
    for i in range(1,len(f)-2):
        if(f[i]+f[i+1] +f[i+2] > prev):
            gratest+=1
        prev = f[i]+f[i+1] +f[i+2]
    print(gratest)
    


solution()