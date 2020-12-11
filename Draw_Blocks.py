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

#Function to draw the blocks in a grid pattern
def blocks():
	x0 = 10
	x1 = 30
	y0 = 10
	y1 = 30
	global blocks
	blocks = [0]*133
	n=0
	# To position the blocks in a grid like pattern
	for i in range(7):
		for j in range(19): 
			blocks[n] = canvas.create_rectangle(x0,y0,x1,y1, fill= "orange")
			canvas.pack()
			x0 = x0 + 20
			x1 = x1 + 20
			n = n+1
		x0 = 10
		x1 = 30
		y0 = y0 + 20
		y1 = y1 + 20

blocks()
window.mainloop()