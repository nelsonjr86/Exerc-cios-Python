file_name = input("Digite o nome do arquivo: ")
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("A partir de ")]
who_from_dict = {}
for line in lines:
    words = line.split()
    who_from_dict[words[1]] = who_from_dict.get(words[1], 0) + 1
most = 0
winner = None
for person in who_from_dict:
    if who_from_dict[person] > most:
        most = who_from_dict[person]
        winner = person
print (winner, who_from_dict[winner])