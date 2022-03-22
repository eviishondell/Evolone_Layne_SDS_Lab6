#Evolone Layne and Taiwo Oriowo
from flask import Flask
from flask import render_template
from flask import request
from model import capital_check


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return "Finish quiz to see answers"
    else:
        answers = { "new york": request.form['New York'], 
                    "california": request.form['California'],
                    "utah": request.form['Utah'],
                    "alabama": request.form['Alabama'],
                    "ohio": request.form['Ohio'],
                    }
        graded_answers = capital_check(answers)
        new_york_answer = graded_answers['new york']
        california_answer = graded_answers['california']
        utah_answer = graded_answers['utah']
        alabama_answer = graded_answers['alabama']
        ohio_answer = graded_answers['ohio']
        

        return render_template('results.html', new_york_answer = new_york_answer,
        california_answer = california_answer, utah_answer = utah_answer,
        alabama_answer = alabama_answer, ohio_answer = ohio_answer)
