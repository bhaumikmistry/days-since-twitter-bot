from InstagramAPI import InstagramAPI
from secret import UN
from secret import PW
from days_since import data
from generate_image import GenerateImage

if __name__ == "__main__":
    InstagramAPI = InstagramAPI(UN,PW)
    if(InstagramAPI.login()):
        print("login() oK")
        d = data()
        caption = d.get_string()
        gi = GenerateImage(caption)
        photo_path = gi.generate_image()
        InstagramAPI.uploadPhoto(photo=photo_path,caption=caption)