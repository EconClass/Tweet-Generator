from dictogram import Dictogram
from cleanup import clean_text
from listogram import Listogram
from sample import *
import random

def first_order(clean_text):
    markov_dict = {}
    for index in range(len(clean_text) - 1):
        check = clean_text[index]        
        if check not in markov_dict:      
            markov_dict[check] = Dictogram()
        markov_dict[check].add_count(clean_text[index+1])
    return markov_dict

def random_walk_first(clean_text, sen_len=10):
    initial = dictionary_sample(Dictogram(clean_text))
    sentence = [initial]
    markov = first_order(clean_text)
    count = 0
    index = 0

    while count < sen_len:
        window = sentence[index]
        add = dictionary_sample(markov[window])
        if add is not None:
            sentence.append(add)
            count += 1
            index += 1
    return ' '.join(sentence)

def second_order(clean_text):
    markov = {}
    length = len(clean_text)
    for index in range(length - 2):
        if index + 2 < length:
            markv_type = (clean_text[index], clean_text[index + 2])
        if markv_type not in markov:
            markov[markv_type] = Dictogram()
        markov[markv_type].add_count(clean_text[index + 2])
    return markov

def main():
    corpus = clean_text('book_1.txt')
    print(random_walk_first(corpus))
    
if __name__ == '__main__':
    main()