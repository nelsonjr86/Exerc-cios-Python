count = 0
total = 0.0
while 1 :
    inp = input ('Insira um número: ')
    if 'done' == inp :
        break
    try:
        total = total + float(inp)
        count = count + 1
    except:
        print ('Entrada invalida')
# Evita divisão por zero
if 0 < count :
    print ('Total:', total, ' Contagem:', count, ' Media', total/count)
else:
    print ('Nenhum numero inserido')