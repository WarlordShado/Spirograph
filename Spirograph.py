import tkinter as tk
from tkinter import IntVar, ttk
import turtle

def main():
    canvas = turtle.getcanvas()
    turtle.bgcolor("black")
    root = canvas.master
    root.title("Spirograph")

    buttonFrame = ttk.Frame(root,width = 100,height = 100)

    moveTurtle = ttk.Button(buttonFrame,text = "Move Turtle!", command = move)
    moveTurtle.grid(row = 0, column = 0,padx = 5,pady = 5)
    stopTurtle = ttk.Button(buttonFrame,text = "Stop Turtle!", command = stop)
    stopTurtle.grid(row = 0, column = 1,padx = 5,pady = 5)
    resetTurtle = ttk.Button(buttonFrame,text = "Reset Turtle", command = reset)
    resetTurtle.grid(row = 0, column = 2, padx = 5,pady = 5)

    n = tk.StringVar()
    global selectShape
    selectShape = ttk.Combobox(buttonFrame,width = 15,height = 100, textvariable = n)
    selectShape.grid(row = 1, column = 0, columnspan = 3,padx = 5, pady = 5)
    selectShape['values'] = ("Spiral","Star","Triangle","Circle")

    lblOffset = ttk.Label(buttonFrame, text = "Offset: ")
    lblOffset.grid(row = 2, column = 0, pady = 5,padx = 5)

    global txtOffset
    txtOffset = tk.Text(buttonFrame,width = 15,height = 1)
    txtOffset.grid(row = 2, column = 1, padx = 5, pady = 5)
    
    buttonFrame.pack(before = canvas)

    turtle.mainloop()

def reset():
    turtle.clear()
    turtle.reset()
    turtle.done()

def stop():
    turtle.done()

def move():
    colorCount = 0
    colors = ["red","orange","yellow","lime","cyan","magenta"]
    turtle.speed(50)

    shape = tk.StringVar()
    shape = selectShape.get()
    offset = int(txtOffset.get("1.0",tk.END))
    turtle.shape("circle")
    turtle.shapesize(.25,.25,.25)
    
    match(shape):
        case "Spiral":
            for steps in range(150):
                for color in colors:
                    turtle.color(color)
                    turtle.forward(steps * 3)
                    turtle.right(offset)
                    #turtle.stamp()
        case "Star":
            forwardAmt = 60
            
            for multiplyer in range(60):
                if colorCount > len(colors) - 1:
                    colorCount = 0

                turtle.color(colors[colorCount])

                for steps in range(5):
                    turtle.forward(forwardAmt * (multiplyer + 1))
                    turtle.right(144)
                    #turtle.stamp()

                #Changes the color for the Next star
                colorCount += 1

                #Moves the pen to draw the next star
                turtle.penup()
                turtle.forward((forwardAmt / 2) * -1)
                turtle.right(90)
                turtle.forward(-10)
                turtle.left(offset)
                turtle.pendown()
        case "Triangle":
            turtle.penup()
            turtle.forward(40)
            turtle.right(60)
            turtle.pendown()

            for multiplyer in range(60):
                for triangles in range(6):

                    if colorCount > len(colors) - 1:
                        colorCount = 0

                    turtle.color(colors[colorCount])

                    for steps in range(3):
                    
                        turtle.right(120)
                        turtle.forward(25 * (multiplyer + 1))
                        #turtle.stamp()

                    colorCount += 1

                    turtle.penup()
                    turtle.forward(-20)
                    turtle.right(offset)
                    turtle.pendown()
        case "Circle":
            colorCount = 0
            
            for rad in range(250):
                turtle.color(colors[colorCount])
                
                if rad % 4 == 0:
                    colorCount += 1

                if colorCount > len(colors) - 1:
                    colorCount = 0
                
                turtle.circle(rad)
                turtle.penup()
                turtle.right(offset)
                turtle.pendown()

main()