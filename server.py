from os import environ
from flask import Flask
from main import Test

app = Flask(__name__)

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