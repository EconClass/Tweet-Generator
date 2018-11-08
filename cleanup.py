def clean_text(source_text):
    '''
    This function accesses a source file and uses punctuation_table to 
    remove punctuations and special characters.
    '''

    # Creates table of punctuations for comparison
    punctuation_table = str.maketrans( '\n-' , '  ', '''1234567890~!@#$.,%^&*()_+?/`[];'":|''' )
    
    # Opens file and removes characters based on punctuation_table
    text = open(source_text)
    text_list = text.read().translate(punctuation_table).replace('--', ' ')
    text.close()
    
    # Splits text into list and lowers case of all items
    text_list = text_list.lower().split()

    # Creates NEW list of same items with out whitespace on ends
    text_list = [ item.strip() for item in text_list ]

    return text_list