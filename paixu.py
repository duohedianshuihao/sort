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
			time.sleep(0.01)
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
		

def MergeSort(L, rectangle, draw_on):
	if len(L) <= 1:	return L, rectangle
	n = int(len(L)/2)
	left, left_rectangle = MergeSort(L[:n], rectangle[:n], draw_on)
	right, right_rectangle = MergeSort(L[n:], rectangle[n:], draw_on)
	l, r = 0, 0
	result = []
	result_rectangle = []
	while l < len(left) and r < len(right) :
		draw_on.itemconfig(left_rectangle[l], fill = 'red')
		draw_on.itemconfig(right_rectangle[r], fill = 'red')
		draw_on.update()
		time.sleep(0.05)
		if left[l] > right[r] :
			result.append(left[l])
			result_rectangle.append(left_rectangle[l])
			time.sleep(0.05)
			draw_on.itemconfig(left_rectangle[l], fill = 'blue')
			draw_on.update()
			l += 1
			if r == len(right)-1 :
				draw_on.itemconfig(right_rectangle[r], fill = 'blue')
				draw_on.update()
		else :  
			result.append(right[r])
			result_rectangle.append(right_rectangle[r])
			draw_on.itemconfig(left_rectangle[l], fill = 'blue')
			draw_on.move(right_rectangle[r], -6*(len(left)-l), 0)
			for i in xrange(l, len(left)):
				draw_on.move(left_rectangle[i], 6, 0)
			time.sleep(0.025)
			draw_on.itemconfig(right_rectangle[r], fill = 'blue')
			draw_on.update()
			time.sleep(0.025)
			r += 1	
	for x in xrange(0,len(left)):
		draw_on.itemconfig(left_rectangle[x], fill = 'green')
		draw_on.itemconfig(right_rectangle[x], fill = 'green')
		draw_on.update()
	time.sleep(0.1)
	for x in xrange(0,len(left)):
		draw_on.itemconfig(left_rectangle[x], fill = 'blue')
		draw_on.itemconfig(right_rectangle[x], fill = 'blue')
		draw_on.update()
	result += left[l:]
	result += right[r:]
	result_rectangle += left_rectangle[l:]
	result_rectangle += right_rectangle[r:]
	return result, result_rectangle    


def QuickSort(L, rectangle, draw_on):
	return quick_sort(L, 0, len(L)-1, rectangle, draw_on)

def quick_sort(L, left, right, rectangle, draw_on):
	if left >=right: return L
	key = L[left]
	draw_on.itemconfig(rectangle[left], fill = 'green')
	draw_on.update()
	lp = left
	rp = right
	while lp < rp : 
		if lp != left :
			draw_on.itemconfig(rectangle[lp], fill = 'red')
		draw_on.itemconfig(rectangle[rp], fill = 'red')
		draw_on.update()
		time.sleep(0.01)
		while L[rp] <= key and lp < rp :
			draw_on.itemconfig(rectangle[rp], fill = 'blue')
			rp -= 1
			draw_on.itemconfig(rectangle[rp], fill = 'red')
			draw_on.update()
		while L[lp] >= key and lp < rp :
			if lp != left:
				draw_on.itemconfig(rectangle[lp], fill = 'blue')
			lp += 1
			draw_on.itemconfig(rectangle[lp], fill = 'red')
			draw_on.update()
		L[lp], L[rp] = L[rp], L[lp]
		draw_on.move(rectangle[lp], 6*(rp-lp), 0)
		draw_on.move(rectangle[rp], 6*(lp-rp), 0)
		draw_on.update()
		rectangle[lp], rectangle[rp] = rectangle[rp], rectangle[lp]
	L[left], L[lp] = L[lp], L[left]
	draw_on.move(rectangle[left], 6*(lp-left), 0)
	draw_on.move(rectangle[lp], 6*(left-lp), 0)
	draw_on.itemconfig(rectangle[lp], fill = 'blue') 
	draw_on.itemconfig(rectangle[left], fill = 'blue')
	draw_on.update()
	rectangle[left], rectangle[lp] = rectangle[lp], rectangle[left] 
	quick_sort(L, left, lp-1, rectangle, draw_on)
	for x in xrange(lp-1, rp+2):
		time.sleep(0.0001)
		draw_on.itemconfig(rectangle[x], fill = 'green')
		draw_on.update()
	quick_sort(L, rp+1, right, rectangle, draw_on)
	return L  
 
def HeapSort(L, rectangle, draw_on):
	n = len(L)
	first = int(n/2-1)       
	for start in xrange(first, -1, -1) :     
		max_heapify(L,start, n-1, rectangle, draw_on)
	for end in xrange(n-1, 0, -1):           
		L[end], L[0] = L[0], L[end]
		draw_on.move(rectangle[0], 6*(end-0), 0)
		draw_on.move(rectangle[end], 6*(0-end), 0)
		draw_on.update()
		rectangle[0], rectangle[end] = rectangle[end], rectangle[0]
		max_heapify(L, 0, end-1, rectangle, draw_on)
	return L
 
def max_heapify(L, start, end, rectangle, draw_on) :
	root = start
	while True :
		child = root*2 +1               
		time.sleep(0.01)
		if child > end : break
		if child+1 <= end and L[child] > L[child+1] :
			child = child+1            
		if L[root] > L[child] :    
			L[root], L[child] = L[child], L[root]
			draw_on.move(rectangle[root], 6*(child-root), 0)   
			draw_on.move(rectangle[child], 6*(root-child), 0)
			draw_on.update()
			rectangle[root], rectangle[child] = rectangle[child], rectangle[root]
			root = child
		else :
			break  
  
 
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

def Button_MergeSort():
	draw_on.delete("all")
	L = generate_array()
	MergeSort(L, draw(L, draw_on), draw_on)

def Button_QuickSort():
	draw_on.delete("all")
	L = generate_array()
	QuickSort(L, draw(L, draw_on), draw_on)
def Button_HeapSort():
	draw_on.delete("all")
	L = generate_array()
	HeapSort(L, draw(L, draw_on), draw_on)

			
root = Tk()
frame_button = Frame(root)
frame_button.pack(side = TOP)
frame_draw = Frame(root)
frame_draw.pack()
b_Bubble = Button(frame_button, text = "Bubble", width = 4, height = 1, command = Button_BubbleSort).pack(side = LEFT)
b_Select = Button(frame_button, text = "Select", width = 4, height = 1, command = Button_SelectSort).pack(side = LEFT)
b_Insertion = Button(frame_button, text = "Insertion", width = 4, height = 1, command = Button_InsertionSort).pack(side = LEFT)
b_Shell = Button(frame_button, text = "Shell", width = 4, height = 1, command = Button_ShellSort).pack(side = LEFT)
b_Merge = Button(frame_button, text = "Merge", width = 4, height = 1, command = Button_MergeSort).pack(side = LEFT) 
b_Quick = Button(frame_button, text = "Quick", width = 4, height = 1, command = Button_QuickSort).pack(side = LEFT)
b_Heap = Button(frame_button, text = "Heap", width = 4, height = 1, command = Button_HeapSort).pack(side = LEFT)

draw_on = Canvas(frame_draw, bg = 'white', height = 700, width = 1000)
draw_on.pack() 
L = generate_array()
draw(L, draw_on)
root.mainloop() 