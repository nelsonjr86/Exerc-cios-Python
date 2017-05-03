# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

hrs = input('Enter number of hours:  ')
pay = input('Enter rate per hour: ')
soma=(hrs*pay)
print ("Salário Bruto :"+ soma)

## Exercício 2.5
#F = 9*C/5 + 32
print('----Conversor Temperatura Celsius to Fahrenheit----')

c = float(input('Insira a Temperatura em Celsius: ').replace(',', '.'))
f = (9*(c/5)+32)

print('Fahrenheit : {:.2f}'.format(f))


##°C = (°F - 32) / 1,8

print('----Conversor Temperatura Fahrenheit to Celsius----')

f = float(input('Insira a Temperatura em Fahrenheit: ').replace(',', '.'))
c = ((f-32)/1.8)

print('Celsius : {:.2f}'.format(c))


## exercicio 3.1

hrs = input('Enter number of hours:  ')
pay = input('Enter rate per hour: ')

try:
    iHrs = int(hrs)
except:
    print ('Erro! Por favor, digite uma entrada numérica.')
    sys.exit()
    
try:
    fPay = float(pay)
except:
    print ('Erro! Por favor, digite uma entrada numérica.')
    sys.exit()
    
if iHrs > 40:
    print ('Pay is', ((iHrs-40)*fPay*1.5)+(fPay*40))
else:
    print ('Pay is', iHrs*fPay)


## exercicio 3.3
try:
    grade = float(input('Enter score: '))

    if grade < 0.0 or grade > 1.0:
        print ('Pontuação Ruim')
    elif grade >= 0.9:
        print ('A')
    elif grade >= 0.8:
        print ('B')
    elif grade >= 0.7:
        print ('C')
    elif grade >= 0.6:
        print ('D')
    elif grade < 0.6:
        print ('F')    
except:
    print ('Pontuação Ruim') 
    

## exercicio 5.1
## Initialize variables
count = 0
total = 0.0

while 1 :
    inp = input ('Enter a number: ')
    if 'done' == inp :
        break

    try:
        total = total + float(inp)
        # increase count after total to avoid incorrect count increases on bad inputs
        count = count + 1
    except:
        print ('Invalid input')

# Avoid zero division
if 0 < count :
    print ('Total:', total, ' Count:', count, ' Average', total/count)
else:
    print ('No numbers entered')
    
## exercicio 5.2   
# Initialize variables
max_val = None
min_val = None

while 1 :
    inp = input ('Enter a number: ')
    if 'done' == inp :
        break

    try:
        value = float(inp)

        # Check for minimum
        if min_val is None :
            min_val = value
        elif min_val > value :
            min_val = value

        # Check for maximum
        if max_val is None :
            max_val = value
        elif max_val < value :
            max_val = value
            
    except:
        print ('Invalid input')

print ('Maximum:', max_val, ', Minimum:', min_val)



##Exercise 6.5 Take the following Python code that stores a string:‘
str = 'X-DSPAM-Confidence: 0.8475'
##Use find and string slicing to extract the portion of the string after the colon character and then
#use the float function to convert the extracted string into a ?oating point number.
""

string = "X-DSPAM-Confidence: 0.8475"
start_index = string.find(':')
num = string[start_index+1:].strip()
print (float(num))


## Exercise 6.6
string = "Leia o documento sobre os métodos de string no endereço. Você pode querer experimentar algum deles para ter certeza de que funcionam. strip e replace são bastante úteis."

print ("1."+ string.capitalize())
print ("2."+ string.lower())
print ('3.'+ string.replace("o", "a"))
print ('4.'+ string.upper())


