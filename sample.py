import random
from cleanup import clean_text
from dictogram import Dictogram
from listogram import Listogram

def dictionary_sample(histogram_in):
    cap = 0
    for word in histogram_in:
        cap += histogram_in[word]
    value = random.randint(0, cap)

    cume = 0
    for word in histogram_in:
        cume += histogram_in[word]
        if(cume > value):
            return word

def sample_list_O_stuff(histogram_in): # stuff means tuples or lists
    cap = 0
    i = 0
    while i < len(histogram_in):
        cap += histogram_in[i][1]
        i += 1

    value = random.randint(0, cap)

    cume = 0
    index = 0
    while index < len(histogram_in):
        cume += histogram_in[index][1]
        if cume > value:
            return histogram_in[index][0]
        index += 1


if __name__ == "__main__":
    text = clean_text('book_1.txt')
    hist = Dictogram(text)
    list_hist = Listogram(text)
    print(sample_list_O_stuff(list_hist))
    print(dictionary_sample(hist))