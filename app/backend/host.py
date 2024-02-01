from flask import Flask, request
import random
from flask_cors import CORS

DB_SIZE = 100
app = Flask(__name__)
CORS(app)

@app.route("/")
def h():
    return "home pag" 


@app.route("/getWords")
def wordbank():
    #fake word db
    word_db = open("words/trial.txt", "r")
    # bank_size = int(request.args.get('size'))
    bank_size = 25
    lines = word_db.readlines()         
    word_bank = [lines[random.randint(0,DB_SIZE-1)] for i in range(bank_size)]
    word_bank = list(map(str.strip, word_bank))    # strip new lines

    return word_bank

# @app.route("/leaderBoards"):

#http://localhost:8000
if __name__ == "__main__": 
    app.run(host="localhost", port=8000, debug=True)
