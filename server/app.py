#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}' 

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(parameter)
    result = ''
    for number in numbers:
        result += f'{number}\n'
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        answer= num1+num2
    elif operation == "-":
        answer= num1-num2
    elif operation == "*":
        answer= num1*num2
    elif operation == "div":
        answer= num1/num2
    elif operation == "%":
        answer= num1%num2
    
    return f'{answer}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)