# from secret import CK, CSK, AT, AST
from os import environ
CK = environ['CK']
CSK = environ['CSK']
AT = environ['AT']
AST = environ['AST']

import twitter

class Tweetdata():
    def __init__(self,data,path):
        self.text = data
        self.photo_path = path

    def tweet(self):
        api = twitter.Api(consumer_key=CK,consumer_secret=CSK,access_token_key=AT,access_token_secret=AST)
        json = api.PostUpdate(self.text,self.photo_path)
        print(json)
        print("tweeted data {}",format(self.text))

