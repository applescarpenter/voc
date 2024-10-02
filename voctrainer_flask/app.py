from flask import Flask, render_template, request as flask_req, redirect
import requests as req
import json
from random import randint



app = Flask(__name__)

@app.route('/sdfdfh')
def index():
    return 'hi'

# get 
@app.route('/')
def vocab_practise():
    global voc
    request = req.get('http://127.0.0.1:8000/')
    voc = json.loads(request.content)
    return redirect('/vocTest/next')


# get next vocabulary from list
@app.route('/vocTest/next')
def next_vocabulary():

    global current_tested_vocabulary
    random_number = randint(0,randint(0,len(voc))-1)
    current_tested_vocabulary = voc[random_number]
    # remove vocabulary to prevent vocabulary getting asked more than once
    voc.pop(random_number)
    return render_template('voc.html', vocab = current_tested_vocabulary)


@app.route('/vocTest/verify')
def verify():
    answer = flask_req.args.get('answer')
    if answer == current_tested_vocabulary['vocabulary']:
        test_result = 'Correct!'
        return redirect('/vocTest/next')
    else:
        test_result = "False!"
        
    return render_template('voc.html', vocab = current_tested_vocabulary, result=test_result)
    
    