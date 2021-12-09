def solution():
    f = open("/home/igor/COMP/advent-of-code/puzzle16/input.txt", "r")
    f = f.readlines()
    results = [x.replace("\n"," ").split("|")[1] for x in f]
    results = "".join(results).split(" ")
    results = [x for x in results if x!='']
    f = [x.replace("\n"," ").replace("|","").split(" ") for x in f]
    for item in f:
        for j in item:
            if(j==""):
                item.remove("")
    soma = 0
    dicletter = {}
    for linha in f:
        dic = {}
        for code in linha:
            if(len(code)==2):
                    dic[1]= set(code)
            elif(len(code)==4):
                    dic[4]= set(code)
            elif(len(code)==3):
                    dic[7]= set(code)
            elif(len(code)==7):
                    dic[8]= set(code)
        for code in linha:
            if(len(code)==5):
                if(len(set(code).intersection(dic[4]))==2):
                    dic[2] = set(code)

        for code in linha:
            if(len(code)==5):
                if(len(set(code).intersection(dic[2]))==4):
                    dic[3]= set(code)
                elif(len(set(code).intersection(dic[2]))==3):
                    dic[5]= set(code)
        for code in linha:
            if(len(code)==6):
                if(len(set(code).intersection(dic[4]))==4):
                    dic[9] = set(code)
                elif(len(set(code).intersection(dic[5]))==5):
                    dic[6] = set(code)
                elif(len(set(code).intersection(dic[5]))==4):
                    dic[0] = set(code)
        resultado = ""
        for result in results:
            for number,numberset in dic.items():
                if(set(result)==numberset):
                    print("cheguei aqui")
                    resultado+=str(number)
        soma += int(resultado)
    print(soma)
solution()