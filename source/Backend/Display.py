from PIL import Image, ImageDraw, ImageFont
class StatusViewModel:
    #isTemperatures: array of float
    #setTemperature: float
    #agitation: string
    #time: string
    def __init__(self, isTemperatures, setTemperature, agitation, time):
        self.isTemperatures = isTemperatures
        self.setTemperature = setTemperature
        self.agitation = agitation
        self.time = time

    def generateStatusDisplay(self):
        im = Image.new("1",(128,64),0)

        draw = ImageDraw.Draw(im)
        fnt = ImageFont.truetype('consola.ttf', 12)
        row = 2
        col = 2
        #Idea: 2px space at top and left
        draw.text((col,row), "BoJo", font=fnt, fill="white")
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

# demo um es zu callen
#wie gesagt, hässlich, da nie in python garbeitet :D
# create viewmodel
vm = StatusViewModel([23.84658, 76.92383857], 30, "5s-6s", "03:45")
# create view (image) out of viewmodel
im = vm.generateStatusDisplay()
# display picture in picture viewer
im.show();