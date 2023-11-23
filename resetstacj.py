import time
import math
import pyautogui
import tkinter as tk
import os 
import sys

from tkinter import ttk 
from PIL import Image, ImageTk

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")

    def size(self):
        return len(self.items)
# Move the mouse to the initial position and click the mouse then make the circle
def drawingTime():
    pyautogui.moveTo(x_initial, y_initial)
    time.sleep(2)
    x = x_initial
    y = y_initial
    steps = 0
    leftIndex = nums[0]
    nums.append(leftIndex)
    for j in range(num_steps):        
        for i in range(len(nums)):
            print("Current Queue:", queue.items.copy())
            direction = queue.dequeue()
            if (direction =="l"): 
                x -= nums[i] 
            if (direction == "u"): 
                y -= nums[i] 
            if (direction == "r"): 
                x += nums[i] 
            if (direction == "d"): 
                y+= nums[i]
            print(f"Step {i+1}, Direction: {direction}, Distance: {nums[i]}")
            pyautogui.mouseDown()
            pyautogui.moveTo(x, y)
            print(f"{x} and {y}")
            queue.enqueue(direction)
        direction = queue.dequeue()    
        queue.enqueue(direction)
        print("Loop Done")

    # pyautogui.mouseUp()

# Create the queue 
queue = Queue()
nums = []

# Add the directions to the queue 
queue.enqueue("u")
queue.enqueue("r")
queue.enqueue("d")
queue.enqueue("l")

nums.append(10)
nums.append(20)
nums.append(30)



win = tk.Tk()
win.geometry("250x275")
win.title("Circle time")
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))   
imagedir = f"button.png"
original_image = Image.open(imagedir)
photo = ImageTk.PhotoImage(original_image)
ttk.Button(win, text="Click Here", image = photo, command=drawingTime).pack(pady=20)

#actual program
width, height = pyautogui.size()
center_x, center_y = width/2, (height/2)+20 # +20 to account for the taskbar
num_steps = 70



# Calculate the initial position
x_initial = center_x 
y_initial = center_y 

win.mainloop()