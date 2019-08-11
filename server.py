from os import environ
from flask import Flask
from days_since import data
app = Flask(__name__)


@app.route('/')
def hello():
    d = data()
    caption = d.get_string()
    edited_caption = "Days Since India Won A Cricket World Cup: "
    edited_caption += caption
    return edited_caption

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=environ.get('PORT'))