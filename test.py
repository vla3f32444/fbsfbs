from tkinter import *
from random import *
def change_1():
  x=(0,800)
  y=(0,800)
  z=(0,800)
  w=(0,800)
  r = randint(0, 800)
  e = randint(0, 800)
  f = randint(1, 3)

  lst = ['red', 'blue', 'yellow green', 'black,', 'pink', 'purple']
  t = choice(lst)
  if f == 1:
    canvas.create_rectangle(x, y, z, w, fill=t)
  elif f == 2:
    canvas.create_polygon(x, y, z, w, r, e, fill=t)
  elif f == 3:
    canvas.create_oval(x, y, z, w, fill=t)

window = Tk()
canvas = Canvas(window, width= 1000, height = 900, bg = 'white')
canvas.pack()
Button(text='запуск', command=change_1).pack()
 
window.mainloop()