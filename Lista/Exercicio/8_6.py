def find_min_max():
    user_responses = []
    while True:
        try:
            user_input = input("Digite um número: ")
            print ("Digite break para sair.")
            user_input = int(user_input)
        except:
            break
        user_responses.append(user_input)
    print ("Máximo: ", max(user_responses))
    print ("Minimo: ", min(user_responses))
find_min_max()