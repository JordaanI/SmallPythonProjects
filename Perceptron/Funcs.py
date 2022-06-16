import numpy as np
from random import shuffle
import matplotlib.pyplot as plt
from IPython.display import clear_output

def generate_square(size):
    shape = np.zeros((size,size))
    length = np.random.randint(1,size)
    height = length//2
    start_point = np.random.randint(0,size,(1,2))
    lengthsize = start_point[0,0] + length
    heightsize = start_point[0,1] + height
    while lengthsize > size or heightsize > size or length*height < size**2/10 or length*height > size**2/5:
        length = np.random.randint(1,size)
        height = length//2
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

def batch_generate(size,batch):
    training_seq = []
    area_sq = []
    area_tri = []
    for num in range(batch):
        shape_tri, base_tri, height_tri, start_point_tri = generate_triangle(size)
        shape_sq, base_sq, height_sq, start_point_sq = generate_square(size)
        area_sq.append(base_sq*height_sq)
        area_tri.append(0.5*base_tri*height_tri)
        training_seq.append((shape_sq,-1))
        training_seq.append((shape_tri,1))
    shuffle(training_seq)
    return training_seq, np.mean(area_sq), np.mean(area_tri)

def training(amount,size=200,batch=50,desc=True):
    weights = np.zeros(size**2)
    for num in range(amount):
        train_seq, ave_area_sq, ave_area_tri = batch_generate(size,batch)
        while train_seq:
            i = np.random.randint(0,len(train_seq))
            res = weights @ train_seq[i][0].flatten()
            if res > 0:
                res = 1
            elif res < 0:
                res = -1
            
            if res != train_seq[i][1]:
                weights += (train_seq[i][1] - res)*train_seq[i][0].flatten()
            else:
                del train_seq[i]
        clear_output(wait=True)
        plt.imshow(weights.reshape((size,size)))
        plt.title(f'Elements left: {amount-num-1}')
        plt.colorbar()
        plt.show()
    if desc:
        print(f'Training on {2*batch*amount} shapes.\nAverage square area: {ave_area_sq}.\nAverage triangle area: {ave_area_tri}.')
    return weights

def test(runs,amount,weights,size=200):
    stats = []
    for i in range(runs):
        correct = 0
        for j in range(amount):
            shape_tri, base_tri, height_tri, start_point_tri = generate_triangle(size)
            shape_sq, base_sq, height_sq, start_point_sq = generate_square(size)
            res_sq = shape_sq.flatten() @ weights
            res_tri = shape_tri.flatten() @ weights
            if res_sq < 0:
                correct += 1
            if res_tri > 0:
                correct += 1
        stats.append(round((correct/(2*amount))*100))

    print(f'{np.mean(stats)} is the average correct guesses for these weights')
    plt.hist(list(np.sort(stats)), bins=len(np.unique(stats)));
    plt.title(f'Accuracy of perceptron over {runs} runs.');
    plt.xlabel('Accuracy (%)');