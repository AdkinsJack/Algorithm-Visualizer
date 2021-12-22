import time

# Creating our partition function which receives the: data, the end and start of the array, the drawData , and the timeTick
def partition(data, end, start, drawData, timeTick):
    border = end
    pivot = data[start]

    # Calling the drawData function with our data and the color array.
    drawData(data, getColorArray(len(data), end, start, border, border))
    # Sleeping with our timeTick that the user selected
    time.sleep(timeTick)
    
    # Loops through our range of data.
    for j in range(end, start):
        #  If the index is less than the pivot we drawData. 
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), end, start, border, j, True))
            time.sleep(timeTick)
            # Swap the two values
            data[border], data[j] = data[j], data[border]
            # Incremenet the border
            border += 1
        # Call the drawData function with our data and color array.
        drawData(data, getColorArray(len(data), end, start, border, j))
        time.sleep(timeTick)

    drawData(data, getColorArray(len(data), end, start, border, start, True))
    time.sleep(timeTick)

    # Swap the two values
    data[border], data[start] = data[start], data[border]
    
    return border

# The actual function of sorting.
def quick_sort(data, end, start, drawData, timeTick):
    if end < start:
        partitionIdx = partition(data, end, start, drawData, timeTick)

        #LEFT PARTITION
        quick_sort(data, end, partitionIdx-1, drawData, timeTick)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, start, drawData, timeTick)

# getColorArray function taking the data length, end value, start value, border, currIdx, and boolean of isSwapping.
def getColorArray(dataLen, end, start, border, currIdx, isSwapping = False):
    colorArray = []
    # Looping through the range of our data length.
    for i in range(dataLen):
        # Color gray if between end and start - else color white
        if i >= end and i <= start:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        # Color start blue
        if i == start:
            colorArray[i] = 'blue'
        # Color border red
        elif i == border:
            colorArray[i] = 'red'
        # Color current index yellow
        elif i == currIdx:
            colorArray[i] = 'yellow'
        # Color green if conditions are met.
        if isSwapping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray