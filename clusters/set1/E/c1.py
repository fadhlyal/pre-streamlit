def problemE(number) :
    bilangan = number[0]

    satuan = bilangan//10
    puluhan = bilangan%10

    hasil = (satuan*10 + satuan)*100 + (puluhan*10 + puluhan)

    return hasil