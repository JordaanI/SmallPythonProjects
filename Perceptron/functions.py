import numpy as np

def generate_square_size(length,height,size):
    length = length
    height = height
    while height > length or length%2 == 0 or height == 1:
        length = np.random.randint(1,size)
        height = np.random.randint(1,size)
    return length, height

def generate_square(size):
    shape = np.zeros((size,size))
    length, height = generate_square_size(1,1,size)
    start_point = np.random.randint(0,size,(1,2))
    lengthsize = start_point[0,0] + length
    heightsize = start_point[0,1] + height
    while lengthsize > size or heightsize > size or length*height < size**2/10 or length*height > size**2/5:
        length, height = generate_square_size(0,1,size)
        start_point = np.random.randint(1,size,(1,2))
        lengthsize = start_point[0,0] + length
        heightsize = start_point[0,1] + height
    lengthside = range(start_point[0,0], lengthsize)
    heightside = range(start_point[0,1], heightsize)
    for h in heightside:
        for l in lengthside:
            shape[h,l] = 1
    return shape, length, height, start_point

def generate_triangle(size):
    shape = np.zeros((size,size))
    start_point = np.random.randint(1,size,(1,2))
    base = 2*np.random.randint(2,size//2)-1
    height = (1-base)/-2
    lengthsize = start_point[0,0] + base
    heightsize = start_point[0,1] + int(height)+1
    while lengthsize > size or heightsize > size or 0.5*base*height < size**2/10 or 0.5*base*height > size**2/5:
        start_point = np.random.randint(0,size,(1,2))
        base = 2*np.random.randint(2,size//2)-1
        height = (1-base)/-2
        lengthsize = start_point[0,0] + base
        heightsize = start_point[0,1] + int(height)+1
    lengthside = range(start_point[0,0], lengthsize)
    heightside = range(start_point[0,1], heightsize)[::-1]
    for h in heightside:
        for l in lengthside:
            shape[h,l] = 1
        lengthside = lengthside[1:-1]
    return shape, base, height, start_point