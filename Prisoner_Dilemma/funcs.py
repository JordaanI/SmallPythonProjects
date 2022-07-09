import random

def investigate(seq,num,prisoner,count=0):
    if seq[num] != prisoner:
        count += 1
        if count > 0.5*len(seq):
            return 0
        num = seq[num]
        return investigate(seq,num,prisoner,count)
    else:
        return 1

def initialize(n):
    seq = random.sample(range(n),n)
    unique_prisoners = list(range(n))
    return seq, unique_prisoners


def generate_data(num_of_prisoners):
    seq, unique_prisoners = initialize(num_of_prisoners)
    res = []
    while unique_prisoners:
        num = random.choice(unique_prisoners)
        res.append(investigate(seq,num,num))
        unique_prisoners.remove(num)
    if sum(res)/len(res) == 1:
        return 1
    else:
        return 0