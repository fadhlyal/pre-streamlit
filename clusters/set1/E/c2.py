def problemE(number) :
    bilangan = number[0]

    hasil = ((bilangan//10)*10 + (bilangan//10))*100 + ((bilangan%10)*10 + (bilangan%10))

    return hasil