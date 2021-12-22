import time

def bubble_sort(data, drawData, timeSleep):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            # Loop through the range of data twice.
            # Check if j is less than J+1 if it is then swap the two.
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                # Calls the drawData function to color the appropriate data
                drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                # Sleep using the time our user set in our speedScale
                time.sleep(timeSleep)
    # Finally we drawData to set the color to green for the range of our data
    drawData(data, ['green' for x in range(len(data))])
    
