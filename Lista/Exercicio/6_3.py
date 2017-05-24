palavra = 'banana'
def count(palavra, alvo):
    count = 0
    for carta in palavra:
        if carta == alvo:
            count += 1
    print (count)
count(palavra, 'a')