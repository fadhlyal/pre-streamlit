def problemF(number) :
    bilangan = number[0]

    s_bilangan = str(bilangan)
    konsekutif = True

    for i in range(len(s_bilangan)-1) :
        n1 = int(s_bilangan[i])
        n2 = int(s_bilangan[i+1])

        if(n1-n2 != 1 and n1-n2 != -1) :
            konsekutif = False

    return konsekutif