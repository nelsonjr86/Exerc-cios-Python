import sys
grau = 0
def Calcularnota(grau):
    while True:
        try:
            grau = float(input('Digite a pontuação: '))
        except:
            print ("Pontuação ruim")
            sys.exit(1)
        if grau < 0.6 and grau > 0:
            print ("F")
        elif grau >= 0.6 and grau < 0.7:
            print ("D")
        elif grau >= 0.7 and grau < 0.8:
            print ("C")
        elif grau >= 0.8 and grau < 0.9:
            print ("B")
        elif grau >= 0.9 and grau < 1:
            print ("A")
        else:
            print ("Pontuação Ruim, continue.")
Calcularnota(grau)