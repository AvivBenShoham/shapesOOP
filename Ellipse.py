from Shape import Shape
from ClosedCurve import ClosedCurve
from Circle import Circle
import time
import math

class Ellipse(Circle):

    def __init__(self, xRadios,yRadios, center, color,outlineC):  # center is the circle center
        super(Ellipse, self).__init__(xRadios,center,color,outlineC)
        self.yRadios = yRadios

    def moveMe(self,canvas):
        while True:
            canvas.create_oval(self.center[0] - self.radios, self.center[1] + self.yRadios,
                               self.center[0] + self.radios, self.center[1] - self.yRadios, fill="white",
                               outline="white")

            self.center[0] = self.center[0]+3
            self.center[1] = self.center[1]+3
            canvas.create_oval(self.center[0] - self.radios, self.center[1] + self.yRadios,
                               self.center[0] + self.radios, self.center[1] - self.yRadios, fill=self.color,
                               outline=self.outlineColor)

            time.sleep(1/30)

    def moveMe(self,canvas):
        while True:
            canvas.create_oval(self.center[0] - self.radios, self.center[1] + self.yRadios,
                               self.center[0] + self.radios, self.center[1] - self.yRadios, fill="white",
                               outline="white")

            self.changeDirection(canvas)
            if self.direction[1] == 'E':
                if self.direction[0] == 'S':
                    self.center[0] = self.center[0]+3
                    self.center[1] = self.center[1]+3
                else:
                    self.center[0] = self.center[0]+3
                    self.center[1] = self.center[1]-3
            else:
                if self.direction[0] == 'S':
                    self.center[0] = self.center[0]-3
                    self.center[1] = self.center[1]+3
                else:
                    self.center[0] = self.center[0]-3
                    self.center[1] = self.center[1]-3

            canvas.create_oval(self.center[0] - self.radios, self.center[1] + self.yRadios,
                               self.center[0] + self.radios, self.center[1] - self.yRadios, fill=self.color,
                               outline=self.outlineColor)
            time.sleep(1/30)


    def changeDirection(self,canvas):
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        if self.center[1]+self.yRadios >= height:
            self.direction[0] = 'N'
        elif self.center[1]-self.yRadios <= 0:
            self.direction[0] = 'S'
        if self.center[0]+self.radios >= width:
            self.direction[1] = 'W'
        elif self.center[0]-self.radios <= 0:
                self.direction[1] = 'E'


    def calcArea(self):
        return self.radios*self.yRadios*math.pi

    def drawMe(self,canvas):
        canvas.create_oval(self.center[0] - self.radios,self.center[1]+self.yRadios,self.center[0] + self.radios,self.center[1]-self.yRadios,fill = self.color,outline = self.outlineColor)
