def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle14/input.txt", "r")
    f = f.readlines()
    f = "".join(f).split(",")
    f = [int(x) for x in f]
    maior = max(f)
    menor = min(f)
    cost = float('inf')
    horizontal = 0
    for i in range(menor-100,maior+1):
        custoatual = 0
        for j in range(len(f)): 
            delta = ((abs(f[j]-i)+1)*abs((f[j]-i)))/2
            custoatual+=delta
        if(custoatual<cost):
            cost = custoatual    
            horizontal = i

    print(cost,horizontal)

solution()