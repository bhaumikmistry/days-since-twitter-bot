from os import environ
from flask import Flask

app = Flask(__name__)

class Test:
    def __init__(self):
        print("__init__()")

    def Run():
        print("Run()")
        print("Running from class test")

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dsiwawc')
def dsiwawc():
    return "Days since India Won a Work Cup!"
    test = Test()
    test.Run()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get('PORT'))