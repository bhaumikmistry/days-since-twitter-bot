from PIL import Image, ImageDraw, ImageFont
from days_since import Data
from facts import facts as facts
from random import randint

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

    def generate_image_with_facts(self,number,fact):
        # image load white image
        image_data = Image.open('data/white.jpg')
        draw = ImageDraw.Draw(image_data)

        # create font for the number text
        font = ImageFont.truetype('fonts/OpenSans-Light.ttf',size=50)
        x,y = (800,700)

        # message of the number
        message = number 
        color = 'rgb(150,150,150)'
        w, h = draw.textsize(message,font=font)
        draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)

        # max length of line at size 24 is 60
        max_line_length = 60
        word_list = fact.split()
        sentence = []
        line = str("")
        for word in word_list:
            if 1+len(line)+len(word) > max_line_length:
                sentence.append(line)
                line = word
            else:
                if len(line)>0:
                    line = line + " " + word
                else:
                    line = word
        if len(line)>0:
            sentence.append(line)
        
        # print lines to the image
        font_size = 24
        starting_point = [800,800]
        line_space_diff = font_size*2
        for line in sentence:
            font = ImageFont.truetype('fonts/OpenSans-Light.ttf',size=font_size)
            x,y = (starting_point[0],starting_point[1])
            starting_point[1]+=line_space_diff
            message = line
            print(len(message))
            color = 'rgb(50,50,50)'
            w, h = draw.textsize(message,font=font)
            draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)

        # create font for the fact text
        # font = ImageFont.truetype('fonts/OpenSans-Light.ttf',size=24)
        # x,y = (800,800)
        # message = fact
        # print(len(message))
        # color = 'rgb(50,50,50)'
        # w, h = draw.textsize(message,font=font)
        # draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)
        # x,y = (800,848)
        # message = fact
        # print(len(message))
        # color = 'rgb(50,50,50)'
        # w, h = draw.textsize(message,font=font)
        # draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)

        filename = "data/{}.jpg".format("test")
        image_data.save(filename)


if __name__ == "__main__":
    d = Data()
    caption = d.get_string()
    edited_caption = "01345 78901 34567 90123 56789 12345 78901 34567 90123 56789012 12345 78901 34567 90123 6789 12345 78901 34567 78901 34567 90123 6789 12345 78901 34567"
    gi = GenerateImage(edited_caption)

    length = len(facts)
    print('Number of facts -> ' + str(length))
    random_number = randint(0,length-1)
    print('random fact id -> '+ str(random_number))
    print('Fact -> ' + facts[random_number])
    fact = facts[random_number]

    photo_path = gi.generate_image_with_facts("3251",fact)