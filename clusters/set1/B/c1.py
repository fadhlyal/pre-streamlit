def problemB(number) :
    a = number[0]
    b = number[1]

    hasil = "Bukan kelipatan"
    
    if(b%a == 0) :
        hasil = "Kelipatan"
    
    return hasil