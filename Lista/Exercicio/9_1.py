lines = [word.strip('\n') for word in open('words.txt', 'r')]
word_dict = {}
for line in lines:
    words = line.split()
    for word in words:
        word_dict[word] = None
print ("would" in word_dict)
print ("fast" in word_dict)
print ("python" in word_dict)
