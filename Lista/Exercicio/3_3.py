try:
    grau = float(input('Digite a pontuação: '))

    if grau < 0.0 or grau > 1.0:
        print ('Pontuação Ruim')
    elif grau >= 0.9:
        print ('A')
    elif grau >= 0.8:
        print ('B')
    elif grau >= 0.7:
        print ('C')
    elif grau >= 0.6:
        print ('D')
    elif grau < 0.6:
        print ('F')    
except:
    print ('Pontuação Ruim') 