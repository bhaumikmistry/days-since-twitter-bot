from os import environ
from flask import Flask
from main import PostDsiwacwc

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/dsiwacwc/all')
def dsiwawc_all():
    post = PostDsiwacwc()
    post.Post("all")
    return "From(all) :- Days since India Won a Work Cup!"

@app.route('/dsiwacwc/twiter')
def dsiwawc_twiter():
    post = PostDsiwacwc()
    post.Post("tweet")
    return "From(twiter) :- Days since India Won a Work Cup!"

@app.route('/dsiwacwc/instagram')
def dsiwawc_instagram():
    post = PostDsiwacwc()
    post.Post("insta")
    return "From(instagram) :- Days since India Won a Work Cup!"

@app.route('/dsiwacwc/testhook')
def dsiwawc_testhook():
    print(f"Running testhook!!")
    return "From(testhook) :- Test hook success!!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get('PORT'))
