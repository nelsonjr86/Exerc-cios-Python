file_name = input("Which book? ")
# 'huck.txt'
book = open(file_name, 'r')
def prepare_text(raw_book):
    ''' Take file handler as input. Chop off the project Gutenberg header
    and footer. Remove non-alpha characters. Convert all letters to
    lowercase and finally return the entire book as a singe string '''
    start_marker = "*** START OF THIS"
    end_marker = "*** END OF THIS"
    process_text = False
    book_lines = []
    all_letters = ''
    for line in raw_book:
        if line.startswith(start_marker) and process_text is False:
            process_text = True
        if line.startswith(end_marker) and process_text is True:
            process_text = False
        if process_text is True:
            line = ''.join([char for char in line if char.isalpha()])
            line = line.lower()
            book_lines.append(line)
    all_letters = all_letters.join(book_lines)
    return all_letters
condensed_book = prepare_text(book)
letter_histogram = {}
for letter in condensed_book:
    letter_histogram[letter] = letter_histogram.get(letter, 0) + 1
results_list = []
for key in letter_histogram:
    results_list.append((letter_histogram[key], key))
print ("Letter frequency results for:", file_name)
for pair in sorted(results_list, reverse=True):
    print (pair[1], pair[0])