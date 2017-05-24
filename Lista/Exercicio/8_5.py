fname = input("Digite o nome do arquivo: ")
counter = 0
fh = open(fname)
for line in fh :
    line = line.rstrip()
    if not line.startswith('A partir de '): continue        
    words = line.split()
    print (words[1])
    counter +=1
print ("Havia", counter, "Linhas no arquivo com De como a primeira palavra")