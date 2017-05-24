valor_maximo = None
valor_minimo = None
while 1 :
    inp = input ('Insira um número: ')
    if 'done' == inp :
        break
    try:
        value = float(inp)
        # Verificar o mínimo
        if valor_minimo is None :
            valor_minimo = value
        elif valor_minimo > value :
            valor_minimo = value
        # Verificar o Maximo
        if valor_maximo is None :
            valor_maximo = value
        elif valor_maximo < value :
            valor_maximo = value            
    except:
        print ('Entrada inválida')
print ('Máximo:', valor_maximo, ', Mínimo:', valor_minimo)