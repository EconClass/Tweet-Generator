from cleanup import clean_text

def histogram(iterable):
    '''
    This function takes a iterable list as an argument
    and return a histogram data structure that stores each unique item along with
    the number of times the item appears in the source text.
    '''
    # Empty dictionary to be used to log occurances of items
    dictionary = {}

    # List of unique items to be used as keys for dictionary
    unique_list = []
    
    for item in iterable:
        if item not in unique_list:
            unique_list.append(item)

    for item in unique_list:
        occurance = iterable.count(item)
        dictionary[item] = [ str(item) , occurance ]
    
    return dictionary

def frequency( histogram_in, item ):
    '''
    This function takes a item and histogram argument and
    returns the number of times that item appears in a text.
    '''
    if item in histogram_in:
        return histogram_in[item][1]
    else: return 0


def all_items(histogram_in):
    '''Calculates the total number of items in the text.'''
    total = 0
    for item in histogram_in:
        total += histogram_in[item][1]
    return total

if __name__ == "__main__":
    cleaned_text = clean_text('the_book.txt')
    print(histogram(cleaned_text))