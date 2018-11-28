import word_count
import random
from cleanup import clean_text
from word_count import histogram, all_items

def dictionary_sample(histogram_in, num_iter=1):
    '''
    This function takes in a histogram and returns 
    a list of random words from the dictionary 
    '''

    max_num = all_items(histogram_in)
    cume_sum = 0
    words = []
    count = 0

    # Loop counts number of samples taken from dictionary
    while count < num_iter: 
        rand_num = random.randint(1, max_num)

        # Iterate through all keys in dictionary
        for word in histogram_in: 

            # Add number of occurances to cummulative variable 
            cume_sum += histogram_in[word][1]

            # Add word to return list and exit "for" loop
            if cume_sum >= rand_num:
                words.append(word)
                break
        
        # Adds 1 to count after for loop executes
        count +=1
    return words

if __name__ == "__main__":
    text = clean_text('the_book.txt')
    hist = histogram(text)
    # print(cummulative_sample(hist, 9))
    print(dictionary_sample(hist))