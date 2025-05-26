def problemD(tebak) :

    hasil = (tebak[0] == tebak[1]) or (tebak[1]-tebak[0] == 1) or (tebak[0]-tebak[1] == 1) or (tebak[1]-tebak[0] == 5) or (tebak[0]-tebak[1] == 5)
    
    return hasil