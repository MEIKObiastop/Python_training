import tkinter as tk
import turtle
import random

import daiya
import haato
import kurabu
import spaid

def dispDraw():
    t.clear() #前の絵を消す
    random.choice(draw_functions)()

root=tk.Tk()
root.geometry("700x700")

#turtleの画面設定
canvas=turtle.ScrolledCanvas(master=root)
canvas.pack()
screen=turtle.TurtleScreen(canvas)
t=turtle.RawTurtle(screen)

draw_functions=[
    lambda:daiya.draw(t),
    lambda:haato.draw(t),
    lambda:kurabu.draw(t),
    lambda:spaid.draw(t)
]
    
btn=tk.Button(root,text="何が出るかな？",command=dispDraw)

btn.pack()
tk.mainloop()
