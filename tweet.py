# from secret import CK, CSK, AT, AST
from os import environ
CK = environ['CK']
CSK = environ['CSK']
AT = environ['AT']
AST = environ['AST']

import twitter

class tweetdata():
    def __init__(self,data):
        self.text = data

    def tweet(self):
        api = twitter.Api(consumer_key=CK,consumer_secret=CSK,access_token_key=AT,access_token_secret=AST)
        api.PostUpdate(self.text)
        print("tweeted data {}",format(self.text))

