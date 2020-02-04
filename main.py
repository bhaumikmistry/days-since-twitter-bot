from days_since import Data
from generate_image import GenerateImage
from caption_creator import CaptionCreator
from tweet import Tweetdata
from inatgrampost import InstagramPost


class PostDsiwacwc:
    def __init__(self):
        print("PostDsiwacwc __init__()")
    def Post(self):
        print("Posting Data")
        d = Data()
        caption = d.get_string()

        gi = GenerateImage(caption)
        photo_path = gi.generate_image()

        cc = CaptionCreator()
        edited_caption = "Days Since India Won A Cricket World Cup: "
        edited_caption += caption
        add_on = cc.get_caption_add_on()
        edited_caption += add_on

        td = Tweetdata(edited_caption,photo_path)
        ip = InstagramPost(photo_path,edited_caption)
        print("Tweet and instagram object created.")

        # td.tweet()
        # ip.post()

