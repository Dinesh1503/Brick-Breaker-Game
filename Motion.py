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

#Function to check if the ball is touching the blocks 
def checkblocks(pos):
	i = 0
	for block in blocks:
		pos_block = canvas.coords(block)
		if(pos[2] >=  pos_block[0] and pos[0] <= pos_block[2]):
			if(pos[3] >= pos_block[1] and pos[1] <= pos_block[3]):
				canvas.move(blocks[i], 500, 500)
				return True
		i  = i +1
		
# The Ball class
class Ball: 
	#fucntion to draw the ball
	def ball(): 
		global ball
		ball = canvas.create_oval(110,10,130,30,fill="red")
		canvas.move(ball, 150, 150)
		canvas.pack()
	# Function to check if ball is within the window and to bounce the ball of the paddle
	def Bounce():
		x,y = 2,2
		while True:
			global canvas
			base_pos = canvas.coords(base)
			pos = canvas.coords(ball)
			if(pos[3] >= 400): 
				end_text = canvas.create_text(0, 0, text="Game Over", fill="black", font=("Arial Bold", 25), anchor="nw")
				break
			if(pos[1] <= 0):
				y = -y
			if(pos[0] <= 0 or pos[2] >= 400):
				x = -x
			if(pos[2] >=  base_pos[0] and pos[0] <= base_pos[2]):
				if(pos[3] >= base_pos[1] and pos[1] <= base_pos[3]):
					x = -x
					y = -y
			if(checkblocks(pos) == True):
				y = -y
			canvas.move(ball, x, y)
			sleep(0.02)
			canvas.pack()
			window.update()


#function to check the key pressed on the keyboard
def move(event):

	pos = canvas.coords(base)
	ball_pos = canvas.coords(ball)
	x = 10
	if (event.char == "a"):
		if(pos[0] <= 0 or ball_pos[0] == pos[0]):
			canvas.move(base, 0, 0)
		else:
			canvas.move(base, -x, 0)

	elif (event.char == "d"):	
		if(pos[2] >= 400):
			canvas.move(base, 0, 0)
		else:
			canvas.move(base, x, 0)

	elif (event.char == "w"):
		if(pos[1] <= 0 or pos[1] == 200):
			canvas.move(base, 0, 0)
		else:
			canvas.move(base, 0, -x)

	elif (event.char == "s"):
		if(pos[3] >= 400):
			canvas.move(base, 0, 0) 
		else:
			canvas.move(base, 0, x)
	
paddle.draw_base()
Ball.ball()
blocks()
window.bind("<Key>", move)
Ball.Bounce()
window.mainloop()	


