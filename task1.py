
OUTPUT_FILE = 'summary.txt'
FILE_NAME = 'remarks.txt'

with open(OUTPUT_FILE, 'w') as text_file:
    from itertools import count 
    try:

        def wrd_count(string):
            words = string.split()
            count = len(words)
            text_file.write(f'Total words count: {count}\n')
        
        def char_count(string):
            char_total = 0
            for i in string:
                char_total = char_total + 1
            text_file.write(f"Total characters count: {char_total}\n")
        
        def avg_wrd_length(string):

            words = [word for word in string.split() if word]
            average = sum(map(len, words))/len(words)
            text_file.write(f"The average word length: {average:0.1f}\n")

        def avg_sentence_leng(string):
            sents = string.split('.')
            avg_sent = sum(len(x.split()) for x in sents) / len(sents)
            text_file.write(f"The average sentence length: {avg_sent:0.1f}\n\n")
        remarks_di = {}
        def ly_wrd_count(string):
            for word in string.split():
                if word.endswith("ly") == True:
                    if word in remarks_di:
                        remarks_di[word] += 1
                    else:
                        remarks_di[word] = 1
                    string = string.replace(word,'')

        def longest_words_count(lst, K): 
            cnt = count() 
            return sorted(lst, key = lambda w : (len(w), next(cnt)),  
                                        reverse = True)[:K] 

    except:
        text_file.write(f'Unexpected exception.\n')
    with open(FILE_NAME, 'r') as input:
        data = input.read()
        no_punc =  data.translate({ord(c): "" for c in "!@#$%^&*()_+|.,"})
        stat1 = wrd_count(no_punc)
        stat2 = char_count(no_punc)
        stat3 = avg_wrd_length(no_punc)
        stat4 = avg_sentence_leng(no_punc)
        stat5 = ly_wrd_count(no_punc)
        text_file.write("A word distribution of all words ending in 'ly'\n")
        for i in remarks_di:
            text_file.write(f'{i} {remarks_di[i]} \n')
        text_file.write("A list of top 10 longest words in descending order:\n")
        K = 10
        string_to_list = list(no_punc.split())
        
        text_file.write(f'{longest_words_count(string_to_list, K)}')