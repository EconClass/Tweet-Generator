from dictogram import Dictogram
from cleanup import clean_text
import random

def first_order(clean_text):
    markov_dict = {}
    for index in range(len(clean_text) - 1):
        check = clean_text[index]        
        if check not in markov_dict:      
            markov_dict[check] = Dictogram()
        markov_dict[check].add_count(clean_text[index+1])
    return markov_dict

def second_order(clean_text):
    markov_dict = {}
    for index in range( len(clean_text) - 2):
        check = (clean_text[index],clean_text[index + 1])
        # print(check)
        if check not in markov_dict:
            markov_dict[check] = Listogram()
        markov_dict[check].add_count(check)
        
    
if __name__ == '__main__':
    corpus = clean_text('book_1.txt')
    first_markov = first_order(corpus)
    second_order(corpus)
    # markov_gram = [(key, value) for key, value in Dictogram(corpus).items()]
    # print( markov_gram )
    # words, counts = zip(*markov_gram)
    # print(counts)
    # print(sentence(corpus))
    # print(walk_first(first_markov))
    # print( first_order(corpus) )
    # print(histogram(first_markov))
    # print( second_order(corpus) )