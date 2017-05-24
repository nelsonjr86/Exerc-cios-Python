print('----Conversor Temperatura Celsius to Fahrenheit----')
c = float(input('Insira a Temperatura em Celsius: ').replace(',', '.'))
f = (9*(c/5)+32)
print('Fahrenheit : {:.2f}'.format(f))

print('----Conversor Temperatura Fahrenheit to Celsius----')
f = float(input('Insira a Temperatura em Fahrenheit: ').replace(',', '.'))
c = ((f-32)/1.8)
print('Celsius : {:.2f}'.format(c))