from PIL import Image, ImageDraw, ImageFont
import operator

class StatusViewModel:
    #isTemperatures: array of float
    #setTemperature: float
    #agitation: string
    #time: string
    def __init__(self, isTemperatures = [0], setTemperature = 0, agitation = "unknown", time = "00:00"):
        self.isTemperatures = isTemperatures
        self.setTemperature = setTemperature
        self.agitation = agitation
        self.time = time
        
    # writes black text on white background
    # useful for menus
    def drawInversedText(self, draw, xy, text, font):
        size = font.getsize(text)
        tillxy = tuple(map(operator.add, xy, size))
        rectanglesize = [xy, tillxy]
        # create white rectangle
        draw.rectangle(rectanglesize, fill="white", outline="white")
        # put black text on top
        draw.text(xy, text, font=font, fill="black")
        
        
    def generateStatusDisplay(self):
        im = Image.new("1",(128,64),0)

        draw = ImageDraw.Draw(im)
        fnt = ImageFont.truetype('consola.ttf', 12)
        row = 2
        col = 2
        #Idea: 2px space at top and left
        #draw.text((col,row), "BoJo", font=fnt, fill="white")
        self.drawInversedText(draw, (col,row), "BoJo", fnt)
        row += 12
        #foreach isTemperature -> display
        tempString = "Temp: "
        for item in self.isTemperatures:
            tempString += "{:.2f}".format(item)
            tempString += " "
        draw.text((col,row), tempString, font=fnt, fill="white")
        row += 12
        #display target Temperature
        draw.text((col,row), "Set : {:.2f}".format(self.setTemperature), font=fnt, fill="white")
        row += 12
        #Display Agitation
        draw.text((col,row), "Move: " + self.agitation, font=fnt, fill="white")
        row += 12
        #Display Time
        draw.text((col,row), "Time: " + self.time, font=fnt, fill="white")
        del draw
        del fnt
        return im
