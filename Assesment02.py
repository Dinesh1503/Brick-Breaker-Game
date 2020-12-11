#For screen resolution, use full screen mode
from tkinter import *  
import tkinter as tk
from tkinter import PhotoImage, Label, Menu
from time import sleep
from random import randint
window = tk.Tk()

# The Paddle class 
class paddle:

	# Function to dtraw the Paddle
	def draw_base():
		global canvas
		canvas = tk.Canvas(window,width="400", height = "400")
		global base
		base = canvas.create_rectangle(0,0,100,10, fill ='blue')
		canvas['bg'] = 'light yellow'
		canvas.move(base, 150, 390)
		canvas.pack()

paddle.draw_base()

window.mainloop()