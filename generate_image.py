from PIL import Image, ImageDraw, ImageFont, ImageFilter
from days_since import Data
from facts import facts as facts
from random import randint
import requests
from io import BytesIO
from images import images as images

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

    def generate_image_with_facts(self,img,number,fact):
        """
        generate image with facts
        param img : PIL image object
        param number : A number to print in the center
        param fact : a string to print below the center number
        """
        # image load white image
        image_data = img
        draw = ImageDraw.Draw(image_data)


        # create font for the number text
        font = ImageFont.truetype('fonts/OpenSans-Light.ttf',size=60)
        x,y = (800,680)

        # message of the number
        message = number 
        color = 'rgb(255,255,255)'
        w, h = draw.textsize(message,font=font)
        draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)

        # max length of line at size 24 is 60
        max_line_length = 45
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
        font_size = 34
        starting_point = [800,800]
        line_space_diff = font_size*2
        for line in sentence:
            font = ImageFont.truetype('fonts/OpenSans-Light.ttf',size=font_size)
            x,y = (starting_point[0],starting_point[1])
            starting_point[1]+=line_space_diff
            message = line
            print(len(message))
            color = 'rgb(250,250,250)'
            w, h = draw.textsize(message,font=font)
            draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)

        font = ImageFont.truetype('fonts/OpenSans-Light.ttf',size=23)
        x,y = starting_point

        # message of the number
        message = "•DSIWACWC•" 
        color = 'rgb(255,255,255)'
        w, h = draw.textsize(message,font=font)
        draw.text(((x-w)/2,(y-h)/2),message,fill=color,font=font)

        filename = "data/{}.jpg".format("test")
        image_data.save(filename)

    def generate_image_from_url(self,link) -> Image:
        """
        generate_image_from_url
        para link: a link of the image to fetch data from
        if the link is invalid the class uses the black.jpg image
        used as the back up image for any image failuer
        """
        # try to get the image from the link
        try:
            response = requests.get(link)
            print(response)
        except:
            # if error, load the 'black.jpg' image 
            # and return the load image
            print("Error in the requesets, Link broken")
            print(link + ' Not valid animore')
            image_data = Image.open('data/black.jpg')
            return image_data

        # if the image is deleted from server,
        # then return the back up image
        if(response.status_code == 404):
            print(link + ' Not valid animore')
            image_data = Image.open('data/black.jpg')
            return image_data

        # if the link is working, load the bytes to image 
        img = Image.open(BytesIO(response.content))

        # crop and resize the image to get the prefect
        # square wihtout any strech effects on the
        # vertical or the horizontal images
        w,h = img.size
        if w>h:w=h
        else: h=w
        img = img.crop((0,0,w,h))
        img = img.resize((800,800))

        # blur the image after resize
        img = img.filter(ImageFilter.GaussianBlur(radius=12))
        data = []
        
        # darken the image by 50 grey values in all channel
        for item in img.getdata():
            data.append((item[0]-50,item[1]-50,item[2]-50))
            
        img.putdata(data)
        # filename = "data/{}.jpg".format("test_url")
        # img.save(filename)
        
        # return the image
        return img

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

    length_images = len(images)
    print('Number of facts -> ' + str(length_images))
    random_number_img = randint(0,length_images-1)
    print('random fact id -> '+ str(random_number_img))
    print('Fact -> ' + images[random_number_img])
    image = images[random_number_img]

    photo_path = gi.generate_image_with_facts(gi.generate_image_from_url(image),caption,"")
    # gi.generate_image_from_url("https://images.unsplash.com/photo-1531415074968-036ba1b575da?ixlib=rb-1.2.1&auto=format&fit=crop&w=747&q=80")