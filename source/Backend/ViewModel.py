# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import operator
class ViewModel:
    SIZE = (128,64)
    FONT = 'consola.ttf'
    def generateView(self):
        raise NotImplementedError( "Should have implemented this" )

    def drawInversedText(self, draw, xy, text, font):
        size = font.getsize(text)
        tillxy = tuple(map(operator.add, xy, size))
        rectanglesize = [xy, tillxy]
        # create white rectangle
        draw.rectangle(rectanglesize, fill="white", outline="white")
        # put black text on top
        draw.text(xy, text, font=font, fill="black")

class StatusViewModel(ViewModel):
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
    
        
        
    def generateView(self):
        im = Image.new("1",self.SIZE,0)

        draw = ImageDraw.Draw(im)
        fnt = ImageFont.truetype(self.FONT, 12)
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

class SetTemperatureViewModel(ViewModel):
    TEXT = "Target Temp"
    def __init__(self, setTemperature = 30.0, step = 0.05):
        self.setTemperature = setTemperature
        self.step = step
    def increase(self):
        self.setTemperature += self.step
    def decrease(self):
        self.setTemperature -= self.step
    def generateView(self):
        im = Image.new("1",self.SIZE,0)
        draw = ImageDraw.Draw(im)
        #Generate 2 Fonts
        smallfnt = ImageFont.truetype(self.FONT, 12)
        bigfnt = ImageFont.truetype(self.FONT, 32)
        row = 6
        # Draw Description Text (centered)
        draw.text(((self.SIZE[0]-smallfnt.getsize(self.TEXT)[0])/2, row), self.TEXT, font=smallfnt, fill="white")
        # 18 Pixels Space
        row += 18
        #Draw cropped temperature
        temp = "{:.2f}".format(self.setTemperature) + chr(176) + "C"
        draw.text(((self.SIZE[0]-bigfnt.getsize(temp)[0])/2, row), temp, font=bigfnt, fill="white")

        del draw
        del smallfnt
        del bigfnt
        return im

class MenuViewModel(ViewModel):
    def __init__(self, menuItems):
        self.menuItems = menuItems
        self.selectedMenuItem = 0

    def next(self):
        self.selectedMenuItem += 1 
        self.selectedMenuItem %= len(self.menuItems)

    def prev(self):
        if (self.selectedMenuItem == 0):
            self.selectedMenuItem = len(self.menuItems) - 1
        else:
            self.selectedMenuItem -= 1

    # currently maximum 5 entries, because of display limitation
    # TODO Scrolling View
    def generateView(self):
        im = Image.new("1",self.SIZE,0)

        draw = ImageDraw.Draw(im)
        fnt = ImageFont.truetype(self.FONT, 12)
        row = 2
        col = 8

        for index,item in enumerate(self.menuItems):
            # Selected Item in Inverse Colors
            if (index == self.selectedMenuItem):
                self.drawInversedText(draw, (col,row), item, fnt)
            # Non Selected Items in Regular color
            else:
                draw.text((col,row), item, font=fnt, fill="white")
            row += 12
        del draw
        del fnt
        return im
