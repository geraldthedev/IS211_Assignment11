from logging import debug
from flask import Flask, redirect
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
import sqlite3 as sqli
import pickle


app = Flask(__name__)


to_do = []
filename = 'list'
tasks={}
@app.route('/', methods =['GET'])
def todolist():

    return render_template('todo.html', to_do=to_do)

@app.route('/submit', methods =['POST', 'GET'])
def submit():
    if request.method == "POST":
     tasks={
         'Task': str(request.form['task']),
        'E-Mail': str(request.form['email']),   
        'Priority':str(request.form['priority'])
     }   
     
     to_do.append(tasks)
    print(to_do)
    return redirect(url_for('todolist'))

@app.route('/save', methods=['POST'])
def save():
    outfile = open(filename, 'wb')
    pickle.dump(to_do,outfile)
    outfile.close()
    return redirect(url_for('todolist'))

@app.route('/clear', methods=['POST'])
def clear():
    del to_do[:]
    return redirect(url_for('todolist'))


@app.route('/delete', methods=['POST'])
def delete():
    to_do.remove(request.form['task'])
    return redirect(url_for('todolist'))
if __name__ == '__main__':
    app.run(port=3000, debug=True)