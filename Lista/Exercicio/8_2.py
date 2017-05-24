user_data = input("Qual arquivo? ")
fhand = open(user_data, 'r')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 3: continue
    if words[0] != 'From' : continue
    print (words[2])