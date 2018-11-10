import word_count
import random
from cleanup import clean_text
from word_count import histogram, all_items

def cummulative_sample(histogram_in, num_iter):
    '''
    This function sums the frequency of the items consecutively
    then appends the value to the list value of the key item.
    '''
    max_len = all_items(histogram_in)
    list_tuples = list(histogram_in.items())

    iterations = 0
    cume_sum = 0
    index = 0
    result = []

    while (iterations < num_iter):
        rand_num = random.randrange( max_len )
        while (cume_sum < rand_num):
            index += 1
            cume_sum += list_tuples[index][1]
            if cume_sum >= rand_num:
                break

        result.append(list_tuples[index][0])
        iterations += 1
    
    return result

def dictionary_sample(histogram_in, num_iter=1):
    '''
    This function takes in a histogram and returns 
    a list of random words from the dictionary 
    '''

    max_num = all_items(histogram_in)
    cume_sum = 0
    words = []
    count = 0

    while count < num_iter: 
        rand_num = random.randint(1, max_num)
        for word in histogram_in:
            cume_sum += histogram_in[word][1]
            if cume_sum >= rand_num:
                words.append(word)
                break
        count +=1
    return words

if __name__ == "__main__":
    text = clean_text('the_book.txt')
    hist = histogram(text)
    # print(cummulative_sample(hist, 9))
    print(dictionary_sample(hist))