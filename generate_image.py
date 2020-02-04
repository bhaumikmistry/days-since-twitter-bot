from PIL import Image, ImageDraw, ImageFont
from days_since import Data

class GenerateImage():
    def __init__(self,text_to_add):
        self.text = text_to_add

    def generate_image(self):
        image_data = Image.open('data/backdrop.jpg')
        draw = ImageDraw.Draw(image_data)
        font = ImageFont.truetype('fonts/OpenSans-Light.ttf',size=70)
        x,y = (800,800)
        message = self.text
        color = 'rgb(0,0,0)'
        w, h = draw.textsize(message,font=font)
        draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)
        filename = "data/{}.jpg".format(self.text)
        image_data.save(filename)
        return filename

    def generate_image_test(self):
        image_data = Image.open('data/backdrop.jpg')
        draw = ImageDraw.Draw(image_data)
        font = ImageFont.truetype('fonts/OpenSans-Light.ttf',size=70)
        x,y = (800,950)
        message = "Days Since India Won"
        color = 'rgb(150,150,150)'
        w, h = draw.textsize(message,font=font)
        draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)
        x,y = (800,1000)
        message = "A Cricket World Cup"
        color = 'rgb(150,150,150)'
        w, h = draw.textsize(message,font=font)
        draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)

        filename = "data/{}.jpg".format("test")
        image_data.save(filename)
        return filename

# if __name__ == "__main__":
#     d = data()
#     caption = d.get_string()
#     edited_caption = "Days Since India Won A Cricket World Cup: "
#     edited_caption += caption
#     gi = GenerateImage(edited_caption)
#     photo_path = gi.generate_image_test()