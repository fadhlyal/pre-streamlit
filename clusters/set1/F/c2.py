def problemF(number) :
    bilangan = number[0]

    s_bilangan = str(bilangan)
    konsekutif = True

    for i in range(len(s_bilangan)-1) :
        if(int(s_bilangan[i])-int(s_bilangan[i+1]) != 1 and int(s_bilangan[i])-int(s_bilangan[i+1]) != -1) :
            konsekutif = False

    return konsekutif