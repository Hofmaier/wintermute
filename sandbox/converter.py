
def convert(flatarray):
    width = 640
    height = 480
    n2darray = []
    for row in range(height):
        rowstart = row * width
        rowend = rowstart + width
        row = flatarray[rowstart : rowend]
        n2darray.append(row)
        
    return n2darray
