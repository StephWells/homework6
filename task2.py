
def retrieve_lines(file_name=''):
    result = []
    with open(file_name, 'r') as text_file:
        line = text_file.readline()
        while line != '':
            result.append(line.rstrip('\n'))
            line = text_file.readline()
    return result


def main():
    READ_THIS_FILE = 'book.txt' #This text file has a quote from a book and also the entire alphabet listed at the end as a way to test the program that it actually counted all letters.
    OUTPUT_FILE = 'summary.txt'
    BEGIN = ord('A')
    END = ord('Z')


    read_text = ' '.join(retrieve_lines(READ_THIS_FILE)).upper() 

    letter_freq = dict()
    for letter in read_text:
        if ord(letter) >= BEGIN and ord(letter) <= END:
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
    letter_freq = sorted(letter_freq.items(), key=lambda item: item[0]) #Without lamda and item only the letter print
    

#check for letters and print final statement
    if len(letter_freq) < (END + 1 - BEGIN):
        letter_freq.append("\nIt doesn't have all letters.")
    else:
        letter_freq.append("\nIt has all letters.")
#Print the output to the summary text file itself
    with open(OUTPUT_FILE, 'w') as text_file:
        for entity in letter_freq:
            str_entity = ''
            if type(entity) is str:
                str_entity = entity
            else:
                for record in entity:
                    str_entity += f'{record} '
            str_entity = str_entity.rstrip(' ') + '\n'
            text_file.write(str_entity)

    print(f"Please see {OUTPUT_FILE} for output.")
     
    pass

if __name__ == '__main__':
    main()
