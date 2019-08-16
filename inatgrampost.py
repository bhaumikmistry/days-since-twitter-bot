from os import environ
from InstagramAPI import InstagramAPI
from secret import UN
from secret import PW
# UN = environ['UN']
# PW = environ['PW']


class InstagramPost():
    def __init__(self,photo,caption):
        self.image = photo
        self.text = caption
    
    def post(self):
        instagramAPI = InstagramAPI(UN,PW)
        if(instagramAPI.login()):
            print("Image Posted with caption {}".format(self.text))
            instagramAPI.uploadPhoto(photo=self.image,caption=self.text)
