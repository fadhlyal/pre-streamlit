def problemC(waktu) :
    jam = waktu[0]
    menit = waktu[1]
    detik = waktu[2]

    w_jam = jam*3600
    w_menit = menit*60

    w_detik = w_jam + w_menit + detik

    return w_detik