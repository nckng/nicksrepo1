from flask import Flask

myflask = Flask(__name__)

@myflask.route('/')
def fun1():
    return 'function 1'

@myflask.route('/hi')
def fun2():
    return 'function 2'

@myflask.route('/bye')    
def fun3():
    return 'function 3'

if __name__ == '__main__':
    myflask.run()
