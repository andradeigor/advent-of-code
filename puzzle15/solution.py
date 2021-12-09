def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle15/input.txt", "r")
    f = f.readlines()
    f = [x.replace("\n"," ").split("|")[1] for x in f]
    f = "".join(f).split(" ")
    f = [x for x in f if x!='']
    print(f)
    result = 0
    for code in f:
        if(len(code) ==2 or len(code)==4 or len(code)==3 or len(code)==7):
            result+=1
    
    print(result)
    exit()
    f = [int(x) for x in f]
    dic = {0:["a","b","c","e","f","g"]
    ,1:["c","g"]
    ,2:["a","c","d","e","g"]
    ,3:["a","c","d","f","g"]
    ,4:["b","c","d","f"]
    ,5:["a","b","d","f","g"]
    ,6:["a","b","d","e","f","g"]
    ,7:["a","c","f"]
    ,8:["a","b","c","d","e","f","g"]
    ,9:["a","b","c","d","f","g"]}

solution()