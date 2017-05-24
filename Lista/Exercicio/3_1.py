horas = float(input("Enter numero de horas:  "))
valorhoras = float(input("Enter valor da hora: "))
Taxa = 1.5
def pagamento(horas, valorhoras):
    pagamento_horaextra = 0
    if horas > 40:
        Horas_extras = horas - 40
        pagamento_horaextra = Horas_extras * valorhoras * Taxa
        pagamento_final = ((horas - Horas_extras) * valorhoras) + pagamento_horaextra
    else:
        pagamento_final = (horas * valorhoras)
    return "Pagamento: " + str(pagamento_final)
print (pagamento(horas, valorhoras))