import random

def investigate(seq,num,prisoner,count=0):
    if seq[num] != prisoner:
        count += 1
        if count > 0.5*len(seq):
            return [0, -1]
        num = seq[num]
        return investigate(seq,num,prisoner,count)
    else:
        return [1,count]

def initialize(n):
    seq = random.sample(range(n),n)
    unique_prisoners = list(range(n))
    return seq, unique_prisoners

def one_run(num_of_prisoners):
    seq, unique_prisoners = initialize(num_of_prisoners)
    res = []
    counts = []
    while unique_prisoners:
        num = random.choice(unique_prisoners)
        res.append(investigate(seq,num,num)[0])
        counts.append(investigate(seq,num,num)[1])
        unique_prisoners.remove(num)
    if sum(res)/len(res) == 1:
        return [1,counts]
    else:
        return [0,counts]

def many_runs(number_of_runs,number_of_prisoners):
    res = []
    counts = []
    for i in range(number_of_runs):
        res.append(one_run(number_of_prisoners)[0])
        counts.append(one_run(number_of_prisoners)[1])
    return res, counts