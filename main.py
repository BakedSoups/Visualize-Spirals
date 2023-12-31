import time
import math
import pyautogui
import tkinter as tk
import os 
import sys
import random

import matplotlib.pyplot as plt
from tkinter import ttk 
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def copy(self): 
        return self.items.copy()

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
    @classmethod
    def from_queue(cls, other_queue):
        new_queue = cls()
        new_queue.items = other_queue.items.copy()
        return new_queue
# fix the visualizTATION TKINTER 

if __name__ == '__main__':
    pass

# on a button click
def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("Past Shapes")
    newWindow.geometry("200x200")
    Label(newWindow,text ="Past Shapes").pack() 

    #load the pattern
    

def visualizeMouseMovement(movement_info):
    # Plotting the mouse movement based on the stored information
    for step_info in movement_info:
        x_positions = [step_info['x']]
        y_positions = [step_info['y']]

        for i in range(len(step_info['direction'])):
            direction = step_info['direction'][i]
            distance = step_info['distance'][i]

            if direction == 'l':
                step_info['x'] -= distance
            elif direction == 'u':
                step_info['y'] -= distance
            elif direction == 'r':
                step_info['x'] += distance
            elif direction == 'd':
                step_info['y'] += distance

            x_positions.append(step_info['x'])
            y_positions.append(step_info['y'])

        plt.plot(x_positions, y_positions, marker='o', linestyle='-')

    plt.title('Mouse Movement')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.show()

# Move the mouse to the initial position and click the mouse then make the shape

def animation(): 
    pass
def drawingTime():
    print(f"ready: {leftIndex.items} {nums.items} {queue.items}")
    pyautogui.moveTo(x_initial, y_initial)

    x = x_initial
    y = y_initial
    
    movement_info = []
    steps = 0 
    drawing = True

    while drawing:
        if(nums.size() % 2 ==0 or nums.size() == 1):
            if steps == 100:
                drawing = False
        steps += 1
        step_info = {'x': x, 'y': y, 'direction': [], 'distance': [], 'leftDist': []}    
        if (steps > 2 and math.isclose(x, x_initial, abs_tol=1e-5) and math.isclose(y, y_initial, abs_tol=1e-5)):
            drawing = False
        
        for i in range(nums.size()+1):
            direction = queue.dequeue()
            distance = nums.dequeue()
            if i == 0:
                leftIndex.enqueue(distance)
                leftDist = leftIndex.dequeue()
            
            if i != nums.size()+1:
                if (direction =="l"): 
                    x -= distance
                if (direction == "u"): 
                    y -= distance
                if (direction == "r"): 
                    x += distance
                if (direction == "d"): 
                    y+= distance
            else: 
                if (direction =="l"): 
                    x -= leftDist
                if (direction == "u"): 
                    y -= distance
                if (direction == "r"): 
                    x += distance
                if (direction == "d"): 
                    y+= distance 

            
            step_info['direction'].append(direction)
            step_info['distance'].append(distance)
            step_info['leftDist'].append(leftDist)

            # pyautogui.mouseDown()
            # pyautogui.moveTo(x, y)
            # print(f"Step {i+1}, Direction: {direction}, Distance: {distance} leftDist: {leftDist}")
            nums.enqueue(distance)
            queue.enqueue(direction)

        movement_info.append(step_info)
    print(steps)
    # pyautogui.mouseUp()
    visualizeMouseMovement(movement_info)

def add_random(event = None):
    num = random.randint(1, 10) * 100
    nums.enqueue(num)
    listbox.insert(tk.END, num)
    entry.delete(0, tk.END)

def save_pattern():
# save current queue to a file  

    with open("pattern.txt", "w") as f:
        f.write(str(nums.items))
        f.write("\n")
        f.write(str(queue.items))
        f.write("\n")
        f.write(str(leftIndex.items))
        f.write("\n")
        f.write(str(x_initial))
        f.write("\n")
        f.write(str(y_initial))
        f.write("\n")
        f.write(str(center_x))
        f.write("\n")
        f.write(str(center_y))
        f.write("\n")
        f.write(str(width))
        f.write("\n")
        f.write(str(height))
        f.write("\n")
        for i in range(leftIndex.size()):
            f.write(str(leftIndex.items[i]))
            f.write("\n")
     
    
def add_num(event = None):
    num = int(entry.get()) * 10
    nums.enqueue(num)
    listbox.insert(tk.END, num) 
    entry.delete(0, tk.END)

def clear_list():
    listbox.delete(0, tk.END)
    nums.items = []

def remove_last_input():
    if nums.size() > 0:
        listbox.delete(tk.END)
        nums.dequeue()

# Create the queue 
queue = Queue()
nums = Queue()
leftIndex = Queue()

# Add the directions to the queue 
queue.enqueue("u")
queue.enqueue("r")
queue.enqueue("d")
queue.enqueue("l")

# Ui stuff
win = tk.Tk()
win.geometry("550x540")
win.title("SPIRAL")


script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))   
imagedir = f"button.png"
original_image = Image.open(imagedir)
photo = ImageTk.PhotoImage(original_image)

# Listbox to display nums
listbox = tk.Listbox(win)
listbox.pack(pady=25)

# Entry for user input
entry = tk.Entry(win)
entry.pack(pady=5)

# Buttons to add nums to the list and initiate drawingTime
add_button = tk.Button(win, text="Add Num", command=add_num)
add_button.pack(side='left', padx=10, pady=5)
entry.bind("<Return>", add_num)

# Button to add random number to the list  
add_button = tk.Button(win, text="Add Random", command=add_random)
add_button.pack(side='left', padx=10, pady=5)
entry.bind("<Return>", add_num)

# Button to initiate drawingTime
initiate_button = ttk.Button(win, text="Start Drawing", command=lambda: drawingTime())
initiate_button.pack(side='left', padx=10, pady=20)

#Button to open a see past Shapes 
past_button = ttk.Button(win, text="Past Shapes", command=lambda: openNewWindow()) 
past_button.pack(side='left', padx=10, pady=20) 


# Buttons for clearing the list and removing the last input
clear_button = tk.Button(win, text="Clear List", command=clear_list)
clear_button.pack(side='left', padx=10, pady=5)

#Remove Last Input  
remove_last_button = tk.Button(win, text="Remove Last Input", command=remove_last_input)
remove_last_button.pack(side='left', padx=10, pady=5)

#save pattern
save_pattern_button = tk.Button(win, text="Save Pattern", command=save_pattern) 
save_pattern_button.pack(side='right', padx=10, pady=5) 


#actual program
width, height = pyautogui.size()
center_x, center_y = width/2, (height/2)+20 # +20 to account for the taskbar

# Calculate the initial position
x_initial = center_x 
y_initial = center_y 


win.mainloop()