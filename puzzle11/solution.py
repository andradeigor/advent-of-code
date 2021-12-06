def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle11/input.txt", "r")
    f = f.readlines()
    f = "".join(f).split(",")
    f = [int(x) for x in f]
    cycles = 18
    for i in range(cycles):
        for index in range(len(f)):
            if(f[index] == 0):
                f.append(8)
                f[index] = 6
            else:
                f[index] -=1
        print(f"day {i+1} have: {len(f)} fishes")



solution()