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

    for i in range(num_steps):
        direction = queue.dequeue()
        distance = nums.dequeue()

        if distance == 20:
                if ((steps) % 4 == 0):
                    if (direction == "l"):
                    x -= distance
                    else:
                        x += distance   
            elif ((steps) % 4 == 1):
                if (direction == "u"):
                    y += distance
                else:  
                    y -= distance
            elif ((steps) % 4 == 2):
                if (direction == "r"):
                    x += distance
                else:
                    x -= distance   
            elif ((steps) % 4 == 3):
                if (direction == "d"):
                    y -= distance
                else:  
                    y += distance

            print(f"Step {i+1}, Direction: {direction}, Distance: {distance}")
            pyautogui.mouseDown()
            pyautogui.moveTo(x, y)
            queue.enqueue(direction)
            nums.enqueue(distance)
            steps += 1

        if distance == 60: 
            if ((steps-1)/4 % 2 == 0):
                if (direction =="l"):
                    x -= distance
                else:
                    x += distance   
            else:  
                if(direction == "u"):
                    y += distance
                else:  
                    y -= distance
            print(f"Step {i+1}, Direction: {direction}, Distance: {distance}")                        
            pyautogui.mouseDown()
            pyautogui.moveTo(x, y)
            queue.enqueue(direction)
            nums.enqueue(distance)
            steps+=1

        if distance == 80:
            print(f"debug {steps-2/4%2}")
            if ((steps-2)/4 % 2 == 0):
                if (direction =="l"):
                    x -= distance
                else:
                    x += distance   
            else:  
                if(direction == "u"):
                    y += distance
                else:  
                    print("down")
                    y -= distance

            print(f"Step {i+1}, Direction: {direction}, Distance: {distance}")
            pyautogui.mouseDown()
            pyautogui.moveTo(x, y)
            queue.enqueue(direction)
            nums.enqueue(distance)
            steps+=1
        if distance == -20:
            if ((steps-3)/4 % 2 == 0):
                if (direction =="l"):
                    x += distance
                else:
                    x -= distance   
            else:  
                if(direction == "u"):
                    y -= distance
                else:  
                    y += distance
            print(f"Step {i+1}, Direction: {direction}, Distance: {distance}")
            pyautogui.mouseDown()
            pyautogui.moveTo(x, y)
            queue.enqueue(direction)
            nums.enqueue(distance) 
            steps+=1
            
        print("Final Queue:", queue.items.copy())
        print("Final Nums:", nums.items.copy())
        print("loop done")
    pyautogui.mouseUp()

# Create the queue 
queue = Queue()
nums = Queue()

# Add the directions to the queue 
queue.enqueue("u")
queue.enqueue("r")
queue.enqueue("d")
queue.enqueue("l")
nums.enqueue(20)
nums.enqueue(60)
nums.enqueue(80)
nums.enqueue(-20)


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
num_steps = 15



# Calculate the initial position
x_initial = center_x 
y_initial = center_y 

win.mainloop()