#For screen resolution, use full screen mode
from tkinter import *  
import tkinter as tk
from tkinter import PhotoImage, Label, Menu
from time import sleep
from random import randint
window = tk.Tk()
canvas = tk.Canvas(window,width="400", height = "400")
canvas['bg'] = 'light yellow'
# The Paddle class 
class paddle:

	# Function to dtraw the Paddle
	def draw_base():
		global canvas
		global base
		base = canvas.create_rectangle(0,0,100,10, fill ='blue')
		canvas.move(base, 150, 390)
		canvas.pack()

# The Ball class
class Ball: 
	#fucntion to draw the ball
	def ball(): 
		global ball
		ball = canvas.create_oval(110,10,130,30,fill="red")
		canvas.move(ball, 150, 150)
		canvas.pack()

Ball.ball()
window.mainloop()