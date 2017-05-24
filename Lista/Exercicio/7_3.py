import sys
dados_usuario = input("Digite o nome do arquivo: ")
if dados_usuario == "na na boo boo":
    print ("NA NA BOO BOO TO YOU - You have been punk'd!")
    sys.exit(0)
try:
    user_file = open(dados_usuario, 'r')
except:
    print ("O arquivo não pode ser aberto: " + dados_usuario)
    sys.exit(1)
Lista_linhas  = [line.strip("\n") for line in user_file]
def count_subject_lines(data):
    subject_count = 0
    for line in Lista_linhas:
        if line.startswith("Subject"):
            subject_count += 1
    print (subject_count)
count_subject_lines(Lista_linhas)