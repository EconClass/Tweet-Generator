from flask import Flask,render_template

from markov import main

app = Flask(__name__)

@app.route('/')
def random_sentence():
    
    return render_template("main.html", sentence = main())

if __name__ == '__main__':
    pass
    # code to run when file is executed