# Author : Areeb Amir
# Created on : 23/12/2022
# https://www.github.com/oneAreebAmir

# Important ---> This is not complete. Need to add more features.
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import ttk, colorchooser
from tkinter import filedialog, messagebox
import PIL.ImageGrab as ImageGrab
from PIL import ImageTk, Image

window = Tk()
window.title('Paint')
window.iconbitmap('favicon.ico')
window.geometry('560x500')
window.minsize(560,500)
window.state('zoomed')

c = Canvas(window, bg='white')
c.pack(fill=BOTH, expand=True)

x = window.winfo_rootx() + c.winfo_x()
y = window.winfo_rooty() + c.winfo_y()
x1 = x + c.winfo_width()
y1 = y + c.winfo_height()

Paint_color = 'black'
current_x, current_y = 0, 0

penwidth = 5

def locate_xy(event):
    global current_x, current_y

    current_x, current_y = event.x, event.y

def addLine(event):
    global current_x, current_y
    
    #How it should look
    c.create_line((current_x, current_y, event.x, event.y), fill=Paint_color, width=slider.get(), capstyle=ROUND, smooth=True)
    current_x, current_y = event.x, event.y

def new_canvas():
    c.delete('all')    

def change_fg():
    global Paint_color
    Paint_color = colorchooser.askcolor()[1]

def change_bg(): 
    color = colorchooser.askcolor()[1]
    c.config(bg=color)

def eraser_com():
    global Paint_color
    Paint_color = 'white'
    slider.set(50)


def save_file():
    global thisfile
    thisfile = filedialog.asksaveasfile()
    ImageGrab.grab().crop((x,y,x1,y1)).save(thisfile)

def save_as():
    try:  
        global filename
        filedialog.SaveFileDialog
        filename = filedialog.asksaveasfilename(defaultextension='.jpg')
        ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
        messagebox.showinfo('Paint say ', 'image is saved as '+ str(filename))
    except:
        messagebox.showinfo('Paint say ', 'Ignored')

def open_file():
        None

def exist():
    window.quit()

c.bind('<Button-1>',locate_xy) 
c.bind('<B1-Motion>', addLine)

brush_color = Button(window, text="Brush Color", bg='white',command=change_fg, width=15, relief=RIDGE)
brush_color.pack(side=LEFT)

bg_color = Button(window, text="Background Color",bg='white', command=change_bg,  width=15,relief=RIDGE)
bg_color.pack(side=LEFT)

slider = ttk.Scale(window, from_=5, to=100, orient=HORIZONTAL)
slider.set(penwidth)
slider.pack(side=RIGHT)

clear_canvas = Button(window, text="Clear Canvas", bg='white',command=new_canvas, width=15,relief=RIDGE)
clear_canvas.pack(side=LEFT)

eraser = Button(window, text="Eraser", bg='white', command=eraser_com, width=15, relief=RIDGE)
eraser.pack(side=LEFT)

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save as', command=save_as)
file_menu.add_command(label='Exist', command=exist)
menu_bar.add_cascade(label='File', menu=file_menu)
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_cascade(label='Undo', command=None,)
run_bar.add_cascade(label='Redo', command=None,)

menu_bar.add_cascade(label='Edit', menu=run_bar)
window.config(menu=menu_bar)

window.mainloop()
