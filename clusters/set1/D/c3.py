def problemD(tebak) :
    adik = tebak[0]
    kakak = tebak[1]
    
    return (adik == kakak) or (kakak-adik == 1) or (adik-kakak == 1) or (kakak-adik == 5) or (adik-kakak == 5)