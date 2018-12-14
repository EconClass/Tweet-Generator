import sys
import string
import random
import cleanup
import tokenize
import word_count
import sample
import dictogram

# define some functions that compose the above modules
from flask import Flask
app = Flask(__name__)

def main():
    text_list = clean_text('the_book')
    dictionary_freq = Dictogram(text_list)

    pass

@app.route('/')
def hello_world():
    return main()



if __name__ == '__main__':
    pass
    # code to run when file is executed