def problemE(N):
    a,b = N[0], N[1]
    if a+b+a*b==111:
        return 'yes'
    else:
        return 'no'