while 1:
          arquivo = input('Informe o nome do arquivo: ')
  if arquivo == "xx":
    print("Fim")
    break
  try:
   ref_arquivo = open(arquivo,"r")
   contador = 0
   dicdata=dict()
   for line in ref_arquivo:
     if line.startswith('From'):
         palavra = line.split()
         if len(palavra) > 4:
           #print(palavra[1])
           horacheia=palavra[5]
           hora=horacheia[horacheia.find(":")-2:2]
           if hora in dicdata:
               dicdata[hora] +=1
           else:
             dicdata[hora] = 2
   tupdict=list()
   for key, val in dicdata.items():
     tupdict.append((key,val))
   tupdict.sort()
   for key, val in tupdict:
       print(key, val)
  except:
    print("Arquivo inexistente!!!")
    exit()