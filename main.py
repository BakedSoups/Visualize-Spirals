import time
import math
import pyautogui
import tkinter as tk
import os 
import sys

import matplotlib.pyplot as plt
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
    @classmethod
    def from_queue(cls, other_queue):
        new_queue = cls()
        new_queue.items = other_queue.items.copy()
        return new_queue
def visualizeMouseMovement(movement_info):
    # Plotting the mouse movement based on the stored information
    for step_info in movement_info:
        x_positions = [step_info['x']]
        y_positions = [step_info['y']]

        for i in range(len(step_info['direction'])):
            direction = step_info['direction'][i]
            distance = step_info['distance'][i]

            if direction == 'l':
                step_info['x'] -= step_info['leftDist'][i]
            elif direction == 'u':
                step_info['y'] -= distance
            elif direction == 'r':
                step_info['x'] += distance
            elif direction == 'd':
                step_info['y'] += distance

            x_positions.append(step_info['x'])
            y_positions.append(step_info['y'])

        plt.plot(x_positions, y_positions, marker='o', linestyle='-', label=f'Step {movement_info.index(step_info) + 1}')

    plt.title('Mouse Movement')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.show()

# Move the mouse to the initial position and click the mouse then make the circle
def drawingTime():
    print(f"ready: {leftIndex.items} {nums.items} {queue.items}")
    pyautogui.moveTo(x_initial, y_initial)
    time.sleep(2)
    x = x_initial
    y = y_initial
    
    movement_info = []
    for j in range(num_steps):   
        step_info = {'x': x, 'y': y, 'direction': [], 'distance': [], 'leftDist': []}     
        for i in range(nums.size()):

            print("Current Queue:", queue.items.copy())
            direction = queue.dequeue()
            distance = nums.dequeue()
            if i == 0:
                leftIndex.enqueue(distance)
                leftDist = leftIndex.dequeue()

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

            pyautogui.mouseDown()
            pyautogui.moveTo(x, y)
            print(f"Step {i+1}, Direction: {direction}, Distance: {distance} leftDist: {leftDist}")
            print(f"{x} and {y}")
            nums.enqueue(distance)
            queue.enqueue(direction)

        nums.enqueue(nums.dequeue())
        movement_info.append(step_info)
        print("Loop Done")

    pyautogui.mouseUp()
    visualizeMouseMovement(movement_info)

# Create the queue 
queue = Queue()
nums = Queue()
leftIndex = Queue()

# Add the directions to the queue 
queue.enqueue("u")
queue.enqueue("r")
queue.enqueue("d")
queue.enqueue("l")

nums.enqueue(20)
nums.enqueue(40)
nums.enqueue(60)
nums.enqueue(50)
nums.enqueue(100)




win = tk.Tk()
win.geometry("250x275")
win.title("SPIRAL")
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))   
imagedir = f"button.png"
original_image = Image.open(imagedir)
photo = ImageTk.PhotoImage(original_image)
ttk.Button(win, text="Click Here", image = photo, command=drawingTime).pack(pady=20)



#actual program
width, height = pyautogui.size()
center_x, center_y = width/2, (height/2)+20 # +20 to account for the taskbar
num_steps = 20



# Calculate the initial position
x_initial = center_x 
y_initial = center_y 

win.mainloop()