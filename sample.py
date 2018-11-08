def cummulative_sample(histogram_in, num_iter):
    '''
    This function sums the frequency of the items consecutively
    then appends the value to the list value of the key item.
    '''
    max_len = all_items(histogram_in)
    rand_num = random.randint( 0, max_len )

    list_tuples = histogram_in.items()

    iterations = 0
    cume_sum = 0

    while (iterations < num_iter):
        for word in histogram_in:
            cume_sum += list_tuples[1]
            if cume_sum >= rand_num:
                break
        iterations += 1
    
    return 