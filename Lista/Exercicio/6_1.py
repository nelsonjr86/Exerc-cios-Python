palavra = "python"
def backwards(palavra):
    index = len(palavra) - 1
    while index >= 0:
        print (palavra[index])
        index -= 1
backwards(palavra)