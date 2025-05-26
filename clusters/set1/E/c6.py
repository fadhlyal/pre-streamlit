def problemE(number) :
    satuan = number[0]//10
    puluhan = number[0]%10

    hasil = (satuan*10 + satuan)*100 + (puluhan*10 + puluhan)

    return hasil