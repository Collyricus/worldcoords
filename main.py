import math
import tkinter
from customtkinter import *
from tkinter import *
from CTkMessagebox import CTkMessagebox

# Functions
def calculate():
    theta_radians = (heading.get() - 90) * (math.pi / 180)
    x2 = x1.get() + scale.get() * distance.get() * math.cos(theta_radians)
    y2 = y1.get() + scale.get() * distance.get() * math.sin(theta_radians)
    x2_round = round(x2)
    y2_round = round(y2)
    CTkMessagebox(title='X2 en Z2', message=f'{x2_round, y2_round}')


def show_frame(frame):
    frame.tkraise()


# Create window object
app = CTk()
app.title('Coordinate Calculator')
app.geometry('1200x750')

set_appearance_mode("dark")

# Row/column config for app
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

# Frames
menu = CTkFrame(app)
help = CTkFrame(app)

for frame in (menu, help):
    frame.grid(row=0, column=0, stick='nsew')

# Row and column config for page 'menu'
menu.rowconfigure(0, weight=1)
menu.rowconfigure(1, weight=3)
menu.rowconfigure(2, weight=1)
menu.rowconfigure(3, weight=1)
menu.rowconfigure(4, weight=1)
menu.rowconfigure(5, weight=1)
menu.rowconfigure(6, weight=1)
menu.rowconfigure(7, weight=1)
menu.rowconfigure(8, weight=1)

menu.columnconfigure(0, weight=1)
menu.columnconfigure(1, weight=1)
menu.columnconfigure(2, weight=1)
menu.columnconfigure(3, weight=1)
menu.columnconfigure(4, weight=1)
menu.columnconfigure(5, weight=1)
menu.columnconfigure(6, weight=1)
menu.columnconfigure(7, weight=1)

# Menu frame
title_label = CTkLabel(menu, text='Coordinate Calculator', font=('Helvetica', 48), text_color="#f7f7f5")
title_label.grid(row=0, column=3, columnspan=2, sticky=S)
subtitle_label = CTkLabel(menu, text='Use the Google Earth ruler tool', font=('Helvetica', 24), text_color="#f7f7f5")
subtitle_label.grid(row=1, column=3, columnspan=2)

x1 = DoubleVar()
x1_label = CTkLabel(menu, text='X1', font=('Helvetica', 24), text_color="#f7f7f5")
x1_label.grid(row=3, column=2)
x1_entry = CTkEntry(menu, textvariable=x1)
x1_entry.grid(row=3, column=3, sticky=W)
y1 = DoubleVar()
y1_label = CTkLabel(menu, text='Z1', font=('Helvetica', 24), text_color="#f7f7f5")
y1_label.grid(row=3, column=4)
y1_entry = CTkEntry(menu, textvariable=y1)
y1_entry.grid(row=3, column=5, sticky=W)

scale = DoubleVar()
scale_label = CTkLabel(menu, text='Scale', font=('Helvetica', 24), text_color="#f7f7f5")
scale_label.grid(row=5, column=1)
scale_entry = CTkEntry(menu, textvariable=scale)
scale_entry.grid(row=5, column=2, sticky=W)
distance = DoubleVar()
distance_label = CTkLabel(menu, text='Distance', font=('Helvetica', 24), text_color="#f7f7f5")
distance_label.grid(row=5, column=3)
distance_entry = CTkEntry(menu, textvariable=distance)
distance_entry.grid(row=5, column=4, sticky=W)
heading = DoubleVar()
heading_label = CTkLabel(menu, text='Heading', font=('Helvetica', 24), text_color="#f7f7f5")
heading_label.grid(row=5, column=5)
heading_entry = CTkEntry(menu, textvariable=heading)
heading_entry.grid(row=5, column=6, sticky=W)

calculate_btn = CTkButton(menu, text="Calculate", width=40, height=16, command=calculate, font=('Helvetica', 21))
calculate_btn.grid(row=7, column=3, columnspan=2)

# Start program
show_frame(menu)
app.mainloop()
