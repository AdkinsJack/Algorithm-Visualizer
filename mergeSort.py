import time

# Merge sort function taking in data, drawData and timeSleep.
def merge_sort(data, drawData, timeSleep):
    # Calling merge_sort_alg with the arguments.
    merge_sort_alg(data,0, len(data)-1, drawData, timeSleep)

# merge_sort_alg function taking data, the left and right point, drawData function and timeSleep.
def merge_sort_alg(data, left, right, drawData, timeSleep):
    if left < right:
        # Finding our middle 
        middle = (left + right) // 2
        # Cal again with our middle in place of right
        merge_sort_alg(data, left, middle, drawData, timeSleep)
        # Call again with our middle+1 in place of left
        merge_sort_alg(data, middle+1, right, drawData, timeSleep)
        # Call the merge function with our arguments and newly created middle.
        merge(data, left, middle, right, drawData, timeSleep)

# Merge function that does the value exchanging.
def merge(data, left, middle, right, drawData, timeSleep):
    # First we call drawData to visualize.
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeSleep)

    # Determine the left part and the right part of our data
    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftId = rightId = 0

    # Loop to swap in range of left, and right + 1.
    for dataId in range(left, right+1):
        if leftId < len(leftPart) and rightId < len(rightPart):
            if leftPart[leftId] <= rightPart[rightId]:
                # Swap the two values and increment leftId
                data[dataId] = leftPart[leftId]
                leftId += 1
            else:
                # Swap the two values and increment rightId
                data[dataId] = rightPart[rightId]
                rightId += 1
        # Otherwise-
        elif leftId < len(leftPart):
            # Assign our data and increment leftId
            data[dataId] = leftPart[leftId]
            leftId += 1
        else:
            # Assign our data and increment rightId
            data[dataId] = rightPart[rightId]
            rightId += 1
    
    # Draw our data with the appropriate colors for the values.
    drawData(data, ["green" if x >= left and x <= right else "grey" for x in range(len(data))])
    time.sleep(timeSleep)

# Getting the color array.
def getColorArray(length, left, middle, right):
    colorArray = []

    # Looping through the range of length and conditionals to assign the appropriate colors.
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("grey")

    return colorArray