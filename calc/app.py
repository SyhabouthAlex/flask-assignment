# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    result = add(a, b)

    return str(result)

@app.route('/sub')
def sub_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def mult_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    result = mult(a, b)

    return str(result)

@app.route('/div')
def div_params():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    result = div(a, b)

    return str(result)

@app.route('/math/<operation>')
def math_operation(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    operations = {
        "add": add(a, b),
        "sub": sub(a, b),
        "mult": mult(a, b),
        "div": div(a, b)
    }

    result = operations[operation]
    return str(result)