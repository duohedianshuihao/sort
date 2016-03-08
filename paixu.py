#from __future__ import division
from Tkinter import *
import random, math, time



def generate_array():
	L = []
	for x in xrange(1,150):
		L.append(4 * x)
	random.shuffle(L)
	return L

def draw(L, Canvas):
	rectangle = []
	for x in xrange(0,149):
		rectangle.append(Canvas.create_rectangle(50 + 6 * x - 5, L[x] + 100, 50 + 6 * x + 1, 700 , fill = 'blue'))
	Canvas.pack()
	return rectangle


def BubbleSort(L, rectangle, draw_on):
	n = len(L)
	for i in xrange(0, n-1):

		for j in xrange(1, n - i):
			draw_on.itemconfig(rectangle[j-1], fill = 'red')
			draw_on.itemconfig(rectangle[j], fill = 'red')
			draw_on.update()
			time.sleep(0.01)

			if L[j - 1] < L[j]:
				L[j - 1], L[j] = L[j], L[j - 1]
				draw_on.move(rectangle[j-1], 6, 0)
				draw_on.move(rectangle[j], -6, 0)
				rectangle[j-1], rectangle[j] = rectangle[j], rectangle[j-1]
				draw_on.itemconfig(rectangle[j-1], fill = 'blue')
				draw_on.update()
			elif L[j-1] > L[j]:
				draw_on.itemconfig(rectangle[j], fill = 'red')
				draw_on.itemconfig(rectangle[j-1], fill = 'blue')
				draw_on.update()
		draw_on.itemconfig(rectangle[n-i-1], fill = 'green')
		draw_on.update()




def SelectSort(L, rectangle, draw_on):
	n = len(L)
	for i in xrange(0, n):
		min = i
		for j in xrange(i+1, n):
			draw_on.itemconfig(rectangle[min], fill = 'red')
			draw_on.itemconfig(rectangle[j], fill = 'red')
			draw_on.update()
			time.sleep(0.05)
			if L[j] > L[min] :
				draw_on.itemconfig(rectangle[min], fill = 'blue')
				draw_on.update()
				min = j
			draw_on.itemconfig(rectangle[j], fill = 'blue')
			draw_on.update()
		L[min], L[i] = L[i], L[min]
		draw_on.move(rectangle[min], -6*(min - i), 0)
		draw_on.move(rectangle[i], 6*(min - i), 0)
		rectangle[min], rectangle[i] = rectangle[i], rectangle[min]
		draw_on.itemconfig(rectangle[i], fill = 'green')
		draw_on.update()

		
def InsertionSort(L, rectangle, draw_on):
	n = len(L)
	for i in xrange(1,n):	
		if L[i] > L[i-1] :
			temp = L[i]
			index = i
			for j in xrange(i-1, -1, -1):
				draw_on.itemconfig(rectangle[j], fill = 'red')
				draw_on.itemconfig(rectangle[j+1], fill = 'red')
				draw_on.update()
				time.sleep(0.01)
				if L[j] < temp :
					L[j+1] = L[j]
					draw_on.move(rectangle[j], 6, 0)
					draw_on.move(rectangle[j+1], -6, 0)
					rectangle[j], rectangle[j+1] = rectangle[j+1], rectangle[j]
					draw_on.itemconfig(rectangle[j+1], fill = 'blue')
					draw_on.update()
					index = j
				else :
					draw_on.itemconfig(rectangle[j+1], fill = 'blue')
					draw_on.itemconfig(rectangle[j], fill = 'blue')
					draw_on.update()
					break
			L[index] = temp
			for k in xrange(0,i+1):
				draw_on.itemconfig(rectangle[k], fill = 'green')
			draw_on.update()

		
def ShellSort(L, rectangle, draw_on):
	n = len(L)
	gap = int(round(n/2))
	while gap > 0 :
		for i in xrange(gap, n):
			temp = L[i]
			j = i
			draw_on.itemconfig(rectangle[j], fill = 'red')
			draw_on.itemconfig(rectangle[j-gap], fill = 'red')
			draw_on.update()
			time.sleep(0.01)
			while (j >= gap and L[j-gap] < temp ) :
				L[j] = L[j-gap]
				draw_on.move(rectangle[j-gap], 6*(gap), 0)
				draw_on.move(rectangle[j], -6*(gap), 0)
				rectangle[j-gap], rectangle[j] = rectangle[j], rectangle[j-gap]
				draw_on.itemconfig(rectangle[j], fill = 'blue')
				draw_on.update()
				j = j - gap
			draw_on.itemconfig(rectangle[j], fill = 'blue')
			draw_on.itemconfig(rectangle[j-gap], fill = 'blue')
			draw_on.update()
			L[j] = temp
		gap = int(round(gap/2))
	while gap == 0:
		for x in xrange(0,n):
			time.sleep(0.001)
			draw_on.itemconfig(rectangle[x], fill = 'green')
			draw_on.update()
		


# def MergeSort(L, rectangle, draw_on):
# 	if len(L) <= 1:	return L, rectangle
# 	n = int(len(L)/2)
# 	left, left_rectangle = MergeSort(L[:n], rectangle[:n], draw_on)
# 	right, right_rectangle = MergeSort(L[n:], rectangle[n:], draw_on)
# 	l, r = 0, 0
# 	result = []
# 	result_rectangle = []
# 	while l < len(left) and r < len(right) :
# 		time.sleep(0.01)
# 		if left[l] > right[r] :
# 			result.append(left[l])
# 			result_rectangle.append(left_rectangle[l])
# 			l += 1
# 		else :  ## ji ou shu kao lv jin qu!!!
# 			result.append(right[r])
# 			result_rectangle.append(right_rectangle[r])
# 			draw_on.move(right_rectangle[r], -6*(len(left)+r-l), 0)
# 			for i in xrange(l, len(left)):
# 				draw_on.move(left_rectangle[i], 6, 0)
# 			for i in xrange(0, r-1):
# 				draw_on.move(right_rectangle[i], 6, 0)
# 			draw_on.update()
# 			r += 1	
# 	result += left[l:]
# 	result += right[r:]
# 	result_rectangle += left_rectangle[l:]
# 	result_rectangle += right_rectangle[r:]
# 	return result, result_rectangle

def Button_BubbleSort():
	draw_on.delete("all")
	L = generate_array()
	BubbleSort(L, draw(L, draw_on), draw_on)

def Button_SelectSort():
	draw_on.delete("all")
	L = generate_array()
	SelectSort(L, draw(L, draw_on), draw_on)

def Button_InsertionSort():
	draw_on.delete("all")
	L = generate_array()
	InsertionSort(L, draw(L, draw_on), draw_on)

def Button_ShellSort():
	draw_on.delete("all")
	L = generate_array()
	ShellSort(L, draw(L, draw_on), draw_on)

	
			
root = Tk() 
frame_button = Frame(root)
frame_button.pack(side = TOP)
frame_draw = Frame(root)
frame_draw.pack()
b_Bubble = Button(frame_button, text = "Bubble", width = 4, height = 1, command = Button_BubbleSort).pack(side = LEFT)
b_Select = Button(frame_button, text = "Select", width = 4, height = 1, command = Button_SelectSort).pack(side = LEFT)
b_Insertion = Button(frame_button, text = "Insertion", width = 4, height = 1, command = Button_InsertionSort).pack(side = LEFT)
b_Shell = Button(frame_button, text = "Shell", width = 4, height = 1, command = Button_ShellSort).pack(side = LEFT)
# b_Shell = Button(root, text = "Shell", width = 4, height = 2, command = Button_ShellSort).pack(side = TOP, fill = Y)
# b_Shell = Button(root, text = "Shell", width = 4, height = 2, command = Button_ShellSort).pack(side = TOP, fill = Y)
# b_Shell = Button(root, text = "Shell", width = 4, height = 2, command = Button_ShellSort).pack(side = TOP, fill = Y)
# b_Shell = Button(root, text = "Shell", width = 4, height = 2, command = Button_ShellSort).pack(side = TOP, fill = Y)

draw_on = Canvas(frame_draw, bg = 'white', height = 700, width = 1000)
draw_on.pack() 
L = generate_array()
draw(L, draw_on)
root.mainloop()