import tkinter
from Polygon import Polygon
from Circle import Circle
from Ellipse import Ellipse
from Rectangle import Rectangle
from IsoscelesTriangle import IsoscelesTriangle
from EquilateralTriangle import EquilateralTriangle
from RightTriangle import RightTriangle
from Square import Square
from Parallelogram import Parallelogram
import time
import random
import threading

top = tkinter.Tk()
colors = ["blue","red","grey","orange","black","yellow"]
shapes =[]
x_place_of_button=0
class TkDisplay:
    def __init__(self):

        self.canvas = tkinter.Canvas(top, bg="white", height=600, width=600)
        self.canvas.pack()
        self.canvas.winfo_height()
        #self.remove_button=tkinter.Menubutton(top,text="remove shape")
       # self.remove_button['menu']= tkinter.Menu(self.remove_button,tearoff=0)
        self.remove_button=tkinter.Menu(top)
        self.menu = tkinter.Menu(top)
        top.config(menu=self.remove_button)
        top.config(menu=self.menu)
        self.createMenu()
        self.shapes = []
       # self.remove_button.option_add()




    def createMenu(self):
        self.menu.add_command(label="Square", command=self.create_square)
        self.menu.add_command(label="Rectangle", command=self.create_rectangle)
        self.menu.add_command(label="Paralleolgram", command=self.create_parallelogram)
        self.menu.add_command(label="Right Triangle", command=self.create_right_triangle)
        self.menu.add_command(label="Isosceles Triangle", command=self.create_isosceles_triangle)
        self.menu.add_command(label="Equilateral Triangle", command=self.create_equilateral_triangle)
        self.menu.add_command(label="Circle", command=self.create_circle)
        self.menu.add_command(label="Ellipse", command=self.create_ellipse)
        self.menu.add_cascade(label="Remove Shape",menu=self.remove_button)


    def create_button_of_shape(self,BG_color,FG_color,name,shape):
        mb = tkinter.Menubutton(top, text=name,bg=BG_color,fg=FG_color,activebackground=BG_color,activeforeground=FG_color)
        mb.place(x=70, y=70)
        mb.menu = tkinter.Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mb.menu.add_command(label="Remove",command=self.remove_shape(shape))
        mb.menu.add_command(label="Freeze",command=shape.animationOff())
        mb.menu.add_cascade(label="edit",command=self.remove_shape(shape))

    def remove_shape(self,shape):
        print ("hi")

    def create_square(self):
        global x_place_of_button
        print("square")
        color = colors[random.randint(0,len(colors)-1)]
        outline_color = colors[random.randint(0,len(colors)-1)]
        button = tkinter.Button(top,text="Square", bg=color,height=1,width=1,fg=outline_color)
        button.place(x=0,y=x_place_of_button)
        button = tkinter.Button(top,text="Square", bg=color,height=1,fg=outline_color)
        button.place(x=20,y=0)
        shapes.append(Square([random.randint(0,1000),random.randint(0,1000)],random.randint(10,100),color,outline_color))
        shapes[len(shapes)-1].drawMe(self.canvas)
        t = threading.Thread(target= shapes[len(shapes)-1].moveMe,args = (self.canvas,))
        t.start()



    def create_rectangle(self):
        print("rectangle")
        color = colors[random.randint(0,len(colors)-1)]
        outline_color = colors[random.randint(0,len(colors)-1)]
        rect = Rectangle([random.randint(0,1000),random.randint(0,1000)],random.randint(10,100),random.randint(10,100),color,outline_color)
        shapes.append(rect)
        shapes[len(shapes) - 1].drawMe(self.canvas)
        self.create_button_of_shape(color,outline_color,"rectangle",rect)
        t = threading.Thread(target=shapes[len(shapes) - 1].moveMe, args=(self.canvas,))
        t.start()

    def create_parallelogram(self):
        print("para")
        color = colors[random.randint(0,len(colors)-1)]
        outline_color = colors[random.randint(0,len(colors)-1)]
        shapes.append(Parallelogram([random.randint(0,1000),random.randint(0,1000)],random.randint(0,90),random.randint(0,100),random.randint(0,100),color,outline_color))
        shapes[len(shapes) - 1].drawMe(self.canvas)
        t = threading.Thread(target=shapes[len(shapes) - 1].moveMe, args=(self.canvas,))
        t.start()

    def create_right_triangle(self):
        print("right_tri")
        color = colors[random.randint(0,len(colors)-1)]
        outline_color = colors[random.randint(0,len(colors)-1)]
        shapes.append(RightTriangle([random.randint(0,1000),random.randint(0,1000)],random.randint(0,100),random.randint(0,100),color,outline_color))
        shapes[len(shapes) - 1].drawMe(self.canvas)
        t = threading.Thread(target=shapes[len(shapes) - 1].moveMe, args=(self.canvas,))
        t.start()

    def create_isosceles_triangle(self):
        print("iso triangle")
        color = colors[random.randint(0,len(colors)-1)]
        outline_color = colors[random.randint(0,len(colors)-1)]
        shapes.append(IsoscelesTriangle([random.randint(0,1000),random.randint(0,1000)],random.randint(0,100),random.randint(0,100),color,outline_color))
        shapes[len(shapes) - 1].drawMe(self.canvas)
        t = threading.Thread(target=shapes[len(shapes) - 1].moveMe, args=(self.canvas,))
        t.start()

    def create_equilateral_triangle(self):
        print("eq triangle")
        color = colors[random.randint(0,len(colors)-1)]
        outline_color = colors[random.randint(0,len(colors)-1)]
        shapes.append(EquilateralTriangle([random.randint(0,1000),random.randint(0,1000)],random.randint(0,100),color,outline_color))
        shapes[len(shapes) - 1].drawMe(self.canvas)
        t = threading.Thread(target=shapes[len(shapes) - 1].moveMe, args=(self.canvas,))
        t.start()

    def create_circle(self):
        print("circle")
        color = colors[random.randint(0,len(colors)-1)]
        outline_color = colors[random.randint(0,len(colors)-1)]
        shapes.append(Circle(random.randint(0,100),[random.randint(0,1000),random.randint(0,1000)],color,outline_color))
        shapes[len(shapes) - 1].drawMe(self.canvas)
        t = threading.Thread(target=shapes[len(shapes) - 1].moveMe, args=(self.canvas,))
        t.start()

    def create_ellipse(self):
        print("ellipse")
        color = colors[random.randint(0,len(colors)-1)]
        outline_color = colors[random.randint(0,len(colors)-1)]
        shapes.append(Ellipse(random.randint(0,100),random.randint(0,100),[random.randint(0,1000),random.randint(0,1000)],color,outline_color))
        shapes[len(shapes) - 1].drawMe(self.canvas)
        t = threading.Thread(target=shapes[len(shapes) - 1].moveMe, args=(self.canvas,))
        t.start()

    #def mainloop(self):
     #   run = True
     #   time.delay(10)

      #  if(run == False):
       #     top.mainloop()

h = TkDisplay()
points = [(0,0),(50,50),(60,10),(300,35)]

top.mainloop()
top.quit()
