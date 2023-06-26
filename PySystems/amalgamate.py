import sys
import time
import serial
import random
import threading
import tb_logger as log
import tkinter as tk

# Globals
command = True

# Finals
BAUD = 9600
TOUT = 1
PORT = 'COM4'

# Utility
DIAGNOSTICS_MODE = False

def get_time(canvas):
    global last_show
    show = str(arduino.readline()).replace("\\r\\n", "").replace("'", "").replace("b", "")
    canvas.itemconfig(var, text=show)

    if last_show != show:
        if show == "6":
            canvas.itemconfig(rect, fill='green')
        else:
            canvas.itemconfig(rect, fill='red')
    last_show = show
    canvas.after(2, get_time, canvas)

def get_arduino():
    return str(arduino.readline()).replace("\\r\\n", "").replace("'", "").replace("b", "")

try:
    arduino = serial.Serial(PORT, BAUD, timeout=TOUT)
    log.lwrite("Python sees arduino on port" + PORT, "i")
except:
    log.lwrite("No device found on port " + PORT, "e")
    sys.exit()

last_show = "6"


# Create the root
root = tk.Tk()
# Create the bg
show =  str(arduino.readline()).replace("\\r\\n", "").replace("'", "").replace("b", "")
# Arise, Canvas
canvas = tk.Canvas(root, width=600, height=500, bg='antiquewhite')
var = canvas.create_text(300, 100, text=show, fill='blue', font=('serif', 20, 'bold'))
# Draw the initial square
rect = canvas.create_rectangle(230, 10, 290, 60,
                                     outline="black", fill="green",
                                     width=2)
last_show = show
get_time(canvas)
canvas.pack()
root.mainloop()


