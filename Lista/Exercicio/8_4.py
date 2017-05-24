fn= input("Digite o nome do arquivo:")
fh = open('romeo.txt')
lst = list()
for line in fh:
    line = line.strip().split()
    for w in line :
       lst.append(w)    
lst2 = sorted(lst)
l3=[]
for i in lst2 :
   if i not in l3:
      l3.append(i)
print (l3)