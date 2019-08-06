from PIL import Image, ImageDraw, ImageFont

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

