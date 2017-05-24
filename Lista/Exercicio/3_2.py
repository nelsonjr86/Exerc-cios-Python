horas = input('Enter numero de horas:  ')

valorhoras = input('Enter valor da hora: ')

Taxa = 1.5

try:

    iHoras = int(horas)

except:

    print ('Erro! Por favor, digite uma entrada numérica.')
    sys.exit()   
try:
    fvalorhoras = float(valorhoras)
except:
    print ('Erro! Por favor, digite uma entrada numérica.')
    sys.exit()    
if iHoras > 40:
    print ('O pagamento é', ((iHoras-40)*fvalorhoras*Taxa)+(fvalorhoras*40))
else:
    print ('O pagamento é', iHoras*fvalorhoras)