from days_since import Data
from generate_image import GenerateImage
from caption_creator import CaptionCreator
from tweet import Tweetdata
from inatgrampost import InstagramPost
from images import images as images
from random import randint

class PostDsiwacwc:
    def __init__(self):
        print("PostDsiwacwc __init__()")
    def Post(self,info):
        print("Posting Data")
        d = Data()
        caption = d.get_string()

        gi = GenerateImage(caption)

        # length = len(facts)
        # print('Number of facts -> ' + str(length))
        # random_number = randint(0,length-1)
        # print('random fact id -> '+ str(random_number))
        # print('Fact -> ' + facts[random_number])
        # fact = facts[random_number]

        length_images = len(images)
        print('Number of facts -> ' + str(length_images))
        random_number_img = randint(0,length_images-1)
        print('random fact id -> '+ str(random_number_img))
        print('image -> ' + images[random_number_img])
        image = images[random_number_img]

        photo_path = gi.generate_image_with_facts(gi.generate_image_from_url(image),caption,"")
        print(photo_path)
        
        cc = CaptionCreator()
        edited_caption = "Days Since India Won A Cricket World Cup: "
        edited_caption += caption
        add_on = cc.get_caption_add_on()
        edited_caption += add_on

        td = Tweetdata(edited_caption,photo_path)
        ip = InstagramPost(photo_path,edited_caption)
        print("Tweet and instagram object created.")

        if info == "tweet":
            td.tweet()
        elif info == "insta":
            if not ip.post():
                print("Error in instagram post()")
        elif info == "all":
            td.tweet()
            if not ip.post():
                print("Error in instagram post()")



