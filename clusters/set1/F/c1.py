def problemF(number) :
    bilangan = number[0]

    konsekutif = True

    while(konsekutif and bilangan >= 10) :
        n1 = bilangan%10
        n2 = (bilangan//10)%10

        konsekutif = (n1-n2 == 1) or (n1-n2 == -1 )

        bilangan = bilangan//10

    return konsekutif