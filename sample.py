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
    # print(max_len)
    list_tuples = list(histogram_in.items())
    # print(list_tuples)

    iterations = 0
    cume_sum = 0
    index = 0
    result = []

    while (iterations < num_iter):
        rand_num = random.randrange( max_len )
        # print(rand_num)
        while (cume_sum < rand_num):
            index += 1
            cume_sum += list_tuples[index][1]
            if cume_sum >= rand_num:
                # print(cume_sum)
                break

        result.append(list_tuples[index][0])
        iterations += 1
    
    return result


text = clean_text('the_book.txt')
hist = histogram(text)
print(cummulative_sample(hist, 9))