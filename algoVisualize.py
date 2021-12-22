from tkinter import *
from tkinter import ttk
import random
from quickSort import quick_sort
from bubbleSort import bubble_sort
from mergeSort import merge_sort

#Initialize our GUI window
root = Tk()
root.title('Sorting Algorithm Visualisations')
root.maxsize(1000, 700)
root.config(bg='gray')

#Variables
select_alg= StringVar()
data = []

# Main drawData function taking in our data and the color
def drawData(data, colorArray):
    #If there is a previous canvas, remove it all
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 20
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # Top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # Bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        #Creating our rectangles with their text and color.
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update()

#Generate function generating random numbers through our set range.
def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    #Appends our numbers to our data list.
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    #Calls the drawData function with our data and color for then range of the length data.
    drawData(data, ['red' for x in range(len(data))]) 

# Begins our algorithm calculations.
def StartAlgorithm():
    global data
    if not data: return

    # Checks for the algorithm description and calls the appropriate algortihm function.
    if algDesc.get() == "Bubble Sort":
        bubble_sort(data, drawData, speedScale.get())
    
    elif algDesc.get() == "Quick Sort":
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
    
    elif algDesc.get() == "Merge Sort":
        merge_sort(data, drawData, speedScale.get())



# Frame and the layout
ui_frame = Frame(root, width= 600, height=200, bg='blue')
ui_frame.grid(row=0, column=0, padx=10, pady=5)

# Creating our grid layout manager
canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface Creation   
#Row0
Label(ui_frame, text="Algorithm: ", bg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algDesc = ttk.Combobox(ui_frame, textvariable=select_alg, values=['Bubble Sort', "Quick Sort", "Merge Sort"])
algDesc.grid(row=0, column=1, padx=3, pady=3)
algDesc.current(0)

speedScale = Scale(ui_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [seconds]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(ui_frame, text="Start", command=StartAlgorithm, bg='gray').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(ui_frame, from_=5, to=30, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(ui_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(ui_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

# Creating a button that calls the event handler of generate to generate our new array of numbers.
Button(ui_frame, text="New Data", command=Generate, bg='gray').grid(row=1, column=3, padx=5, pady=5)

# Begins the mainloop of our tkinter window.
root.mainloop()