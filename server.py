from os import environ
from flask import Flask
from main import PostDsiwacwc

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dsiwawc/all')
def dsiwawc():
    post = PostDsiwacwc()
    post.Post("all")
    return "Days since India Won a Work Cup!"

@app.route('/dsiwawc/twiter')
def dsiwawc():
    post = PostDsiwacwc()
    post.Post("tweet")
    return "Days since India Won a Work Cup!"

@app.route('/dsiwawc/instagram')
def dsiwawc():
    post = PostDsiwacwc()
    post.Post("insta")
    return "Days since India Won a Work Cup!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get('PORT'))