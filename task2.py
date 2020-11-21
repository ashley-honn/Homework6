''' Please use dictionary to keep the count of each letter. 
Read a speech file named “book.txt” that may have multiple lines. 
Then create a “summary.txt” file that has the frequency of each letter, 
case-insensitive, i.e., “a” and “A” are the same letter. 
Each line has a record of the letter and frequency. ''' 

import os 

# output the files and assign write and read
FILENAME = 'book.txt'
OUTPUT_FILE = 'summary2.txt'
READ_MODE = 'r'
WRITE_MODE = 'w'

try:
    out = open(OUTPUT_FILE, WRITE_MODE)
    book_file = open(FILENAME, READ_MODE)
    with out, book_file:
        speech = book_file.read()
        speech = speech.lower()

        count_alpha = {}
        new = {}
        alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        for word in speech:
            if word in count_alpha:
                count_alpha[word] += 1
            else:
                count_alpha[word] = 1
                       
        for word, count in sorted(count_alpha.items()):
            if word in alphabet:
                out.write(f'{word.upper():<3} {count}\n')
            else: pass

        if alphabet.issubset(count_alpha) == True:
            out.write('\nIt has all the letters')
        else: out.write("\nIt doesn't have all the letters")

except OSError:
    print(f'Unable to open {FILENAME}')
    
